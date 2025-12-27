const canvas = document.getElementById('reactor-canvas');
const ctx = canvas.getContext('2d');

// Configuration & State
let atoms = [];
let particles = []; // For explosion effects
let isRunning = true;
let energyOutput = 0;
let coreTemp = 25;
let reactionCount = 0;
let neutronCount = 0;

// User Controls
const controls = {
    atomCount: document.getElementById('atom-count'),
    pressure: document.getElementById('pressure'),
    cooling: document.getElementById('cooling'),
    controlRods: document.getElementById('control-rods')
};

const displays = {
    atomCount: document.getElementById('atom-count-val'),
    pressure: document.getElementById('pressure-val'),
    cooling: document.getElementById('cooling-val'),
    controlRods: document.getElementById('control-rods-val'),
    energy: document.getElementById('energy-output'),
    temp: document.getElementById('core-temp'),
    status: document.getElementById('system-status'),
    neutrons: document.getElementById('neutron-count'),
    reactions: document.getElementById('reaction-count')
};

// Resize Canvas
function resizeCanvas() {
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Atom Class
class Atom {
    constructor(type, x, y) {
        this.type = type; // 'uranium', 'neutron', 'control_rod', 'waste'
        this.x = x || Math.random() * canvas.width;
        this.y = y || Math.random() * canvas.height;
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = (Math.random() - 0.5) * 2;

        // Properties based on type
        if (type === 'uranium') {
            this.radius = 6;
            this.color = '#00ff88'; // Green
            this.mass = 10;
        } else if (type === 'neutron') {
            this.radius = 2;
            this.color = '#00f2ff'; // Cyan
            this.mass = 1;
            this.vx *= 5; // Neutrons are fast
            this.vy *= 5;
        } else if (type === 'control_rod') {
            this.radius = 8;
            this.color = '#555'; // Grey
            this.mass = 100;
            this.vx = 0; // Stationary-ish
            this.vy = 0;
        } else if (type === 'waste') {
            this.radius = 4;
            this.color = '#ffae00'; // Orange
            this.mass = 5;
        }
    }

    update() {
        // Apply Pressure (Speed multiplier)
        const pressureMult = parseInt(controls.pressure.value) / 5;
        // Apply Cooling (Speed dampener)
        const coolingFactor = 1 - (parseInt(controls.cooling.value) / 200);

        let speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);

        // Cap speed based on pressure/cooling
        if (this.type !== 'control_rod') {
            this.x += this.vx * pressureMult * coolingFactor;
            this.y += this.vy * pressureMult * coolingFactor;
        }

        // Wall Collision
        if (this.x < this.radius || this.x > canvas.width - this.radius) this.vx *= -1;
        if (this.y < this.radius || this.y > canvas.height - this.radius) this.vy *= -1;

        // Keep inside bounds
        this.x = Math.max(this.radius, Math.min(canvas.width - this.radius, this.x));
        this.y = Math.max(this.radius, Math.min(canvas.height - this.radius, this.y));
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();

        // Glow effect for active particles
        if (this.type === 'neutron' || this.type === 'uranium') {
            ctx.shadowBlur = 10;
            ctx.shadowColor = this.color;
        } else {
            ctx.shadowBlur = 0;
        }
        ctx.closePath();
        ctx.shadowBlur = 0; // Reset
    }
}

// Simulation Logic
function initSimulation() {
    atoms = [];
    const count = parseInt(controls.atomCount.value);
    const rods = parseInt(controls.controlRods.value);

    // Add Uranium
    for (let i = 0; i < count; i++) {
        atoms.push(new Atom('uranium'));
    }

    // Add Control Rods
    for (let i = 0; i < rods; i++) {
        atoms.push(new Atom('control_rod'));
    }

    // Reset stats
    energyOutput = 0;
    coreTemp = 25;
    reactionCount = 0;
    neutronCount = 0;
}

function checkCollisions() {
    for (let i = 0; i < atoms.length; i++) {
        for (let j = i + 1; j < atoms.length; j++) {
            const a = atoms[i];
            const b = atoms[j];

            const dx = a.x - b.x;
            const dy = a.y - b.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < a.radius + b.radius) {
                handleCollision(a, b, i, j);
            }
        }
    }
}

function handleCollision(a, b, idxA, idxB) {
    // Fission Logic: Neutron hits Uranium
    if ((a.type === 'neutron' && b.type === 'uranium') ||
        (a.type === 'uranium' && b.type === 'neutron')) {

        // Identify the uranium atom
        const uraniumIdx = a.type === 'uranium' ? idxA : idxB;
        const neutronIdx = a.type === 'neutron' ? idxA : idxB;

        // Remove old atoms
        // We splice carefully (higher index first) to avoid shifting issues
        const first = Math.max(uraniumIdx, neutronIdx);
        const second = Math.min(uraniumIdx, neutronIdx);
        atoms.splice(first, 1);
        atoms.splice(second, 1);

        // Create Fission Result
        // 1. Release Energy
        energyOutput += 50;
        coreTemp += 10;
        reactionCount++;

        // 2. Create Waste
        atoms.push(new Atom('waste', a.x, a.y));
        atoms.push(new Atom('waste', a.x, a.y));

        // 3. Release new Neutrons (2-3)
        const newNeutrons = Math.floor(Math.random() * 2) + 2;
        for (let k = 0; k < newNeutrons; k++) {
            atoms.push(new Atom('neutron', a.x, a.y));
        }

        // Screen shake effect
        shakeCanvas(5);
        return;
    }

    // Absorption Logic: Neutron hits Control Rod
    if ((a.type === 'neutron' && b.type === 'control_rod') ||
        (b.type === 'neutron' && a.type === 'control_rod')) {
        const neutronIdx = a.type === 'neutron' ? idxA : idxB;
        atoms.splice(neutronIdx, 1);
        return;
    }

    // Simple Elastic Collision (Bounce)
    // Simplified physics just to keep them moving apart
    const angle = Math.atan2(b.y - a.y, b.x - a.x);
    const speedA = Math.sqrt(a.vx * a.vx + a.vy * a.vy);
    const speedB = Math.sqrt(b.vx * b.vx + b.vy * b.vy);

    a.vx = -Math.cos(angle) * speedA;
    a.vy = -Math.sin(angle) * speedA;
    b.vx = Math.cos(angle) * speedB;
    b.vy = Math.sin(angle) * speedB;
}

// Screen Shake Logic
let shakeDuration = 0;
let shakeIntensity = 0;

function shakeCanvas(intensity) {
    shakeDuration = 10; // Frames
    shakeIntensity = intensity;
}

function applyShake() {
    if (shakeDuration > 0) {
        const dx = (Math.random() - 0.5) * shakeIntensity;
        const dy = (Math.random() - 0.5) * shakeIntensity;
        canvas.style.transform = `translate(${dx}px, ${dy}px)`;
        shakeDuration--;
    } else {
        canvas.style.transform = 'translate(0, 0)';
    }
}

function updateStats() {
    // Decay temp and energy over time
    energyOutput = Math.max(0, energyOutput * 0.99);
    coreTemp = Math.max(25, coreTemp * 0.995);

    // Count neutrons
    neutronCount = atoms.filter(a => a.type === 'neutron').length;

    // Update DOM
    displays.energy.innerText = Math.floor(energyOutput);
    displays.temp.innerText = Math.floor(coreTemp);
    displays.neutrons.innerText = neutronCount;
    displays.reactions.innerText = reactionCount;

    // Status Logic
    if (coreTemp > 2000) {
        displays.status.innerText = "انصهار نووي وشيك!";
        displays.status.className = "status-critical";
        displays.status.style.color = "red";
    } else if (coreTemp > 800) {
        displays.status.innerText = "خطر";
        displays.status.className = "status-warning";
        displays.status.style.color = "orange";
    } else {
        displays.status.innerText = "مستقر";
        displays.status.className = "status-normal";
        displays.status.style.color = "#00ff88";
    }
}

function loop() {
    if (!isRunning) return;

    ctx.fillStyle = 'rgba(0, 0, 0, 0.3)'; // Trail effect
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    atoms.forEach(atom => {
        atom.update();
        atom.draw();
    });

    checkCollisions();
    updateStats();
    applyShake();

    requestAnimationFrame(loop);
}

// Event Listeners
controls.atomCount.addEventListener('input', (e) => {
    displays.atomCount.innerText = e.target.value;
    // Adjust atoms array to match new count (simplified: just reset or add/remove)
    // For better UX, we'll just re-init if drastic change, or add/remove dynamically
    // Here we'll just re-init for simplicity on this slider
    initSimulation();
});

controls.pressure.addEventListener('input', (e) => {
    displays.pressure.innerText = e.target.value;
});

controls.cooling.addEventListener('input', (e) => {
    displays.cooling.innerText = e.target.value + '%';
});

controls.controlRods.addEventListener('input', (e) => {
    displays.controlRods.innerText = e.target.value;
    initSimulation();
});

document.getElementById('inject-neutron').addEventListener('click', () => {
    atoms.push(new Atom('neutron', canvas.width / 2, canvas.height / 2));
});

document.getElementById('reset-sim').addEventListener('click', initSimulation);

// Impact Modal Logic
const modal = document.getElementById('impact-modal');
const closeBtn = document.querySelector('.close-modal');
const showImpactBtn = document.getElementById('show-impact');

showImpactBtn.addEventListener('click', () => {
    modal.classList.remove('hidden');
    calculateImpact();
});

closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
});

function calculateImpact() {
    // Convert "Energy Output" (arbitrary units) to TNT Kilotons
    // Base factor + current output
    const kilotons = (reactionCount * 0.5) + (energyOutput / 10);

    document.getElementById('total-energy').innerText = kilotons.toFixed(2);

    // Simple physics approximations for visuals
    // Fireball radius ~ Y^(0.4)
    const fireball = Math.pow(kilotons, 0.4).toFixed(2);
    // Shockwave ~ Y^(0.33) * constant
    const shockwave = (Math.pow(kilotons, 0.33) * 2).toFixed(2);

    document.getElementById('fireball-radius').innerText = fireball;
    document.getElementById('shockwave-radius').innerText = shockwave;

    // Casualties estimation (arbitrary density)
    const casualties = Math.floor(kilotons * 1500);
    document.getElementById('casualties').innerText = casualties.toLocaleString();

    // Visual Animation
    const blastCircle = document.querySelector('.blast-circle');
    blastCircle.style.width = '0px';
    blastCircle.style.height = '0px';

    setTimeout(() => {
        // Scale visual size based on kilotons (capped for CSS)
        let size = Math.min(300, kilotons * 10);
        if (size < 20) size = 20; // Min size

        blastCircle.style.width = size + 'px';
        blastCircle.style.height = size + 'px';
    }, 100);
}

// Start
initSimulation();
loop();
