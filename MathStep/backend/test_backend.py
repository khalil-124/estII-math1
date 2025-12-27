import requests
import sys

def test_grade():
    url = "http://127.0.0.1:8000/grade"
    
    # Test 1: x+1 == 1+x
    payload1 = {"student_answer": "1+x", "correct_answer": "x+1"}
    try:
        resp = requests.post(url, json=payload1)
        if resp.status_code == 200 and resp.json().get("is_correct") is True:
            print("Test 1 Passed: 1+x == x+1")
        else:
            print(f"Test 1 Failed: {resp.text}")
    except Exception as e:
         print(f"Test 1 Failed with connection error: {e}")

    # Test 2: x+2 != x+1
    payload2 = {"student_answer": "x+2", "correct_answer": "x+1"}
    try:
        resp = requests.post(url, json=payload2)
        if resp.status_code == 200 and resp.json().get("is_correct") is False:
            print("Test 2 Passed: x+2 != x+1")
        else:
            print(f"Test 2 Failed: {resp.text}")
    except:
        print("Test 2 Failed")

if __name__ == "__main__":
    test_grade()
