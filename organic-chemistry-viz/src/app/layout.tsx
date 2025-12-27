import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Organic Chemistry - Interactive Learning",
  description: "Master organic chemistry with interactive 3D molecules, engaging content, and practice quizzes based on Clayden's Organic Chemistry textbook.",
  keywords: ["organic chemistry", "chemistry", "molecules", "3D visualization", "education", "Clayden"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}
