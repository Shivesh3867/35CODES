# Number Theory Toolkit and Health Reminder App

---

## Project Information

- **Name:** Shivesh Pratap Singh  
- **Registration Number:** 25BSA10131  
- **Course:** Bachelor of Technology (B.Tech)  
- **Faculty:** Dr. Hemraj Shobharam Lamkuche  
- **Institution:** VIT Bhopal University  

---

## Introduction

This repository contains two important projects created during the Bachelor of Technology (B.Tech) degree at VIT Bhopal. The goal is to develop programming and problem-solving skills plus promote student wellbeing.

The **Number Theory Toolkit** consists of 34 small standalone Python scripts that explore classic topics in number theory. Each script allows the user to interact by providing input, see the result of computations, and check the execution performance in terms of runtime and memory usage.

The **Health Reminder App** is a lightweight utility that sends desktop notifications at configured intervals to remind students to maintain health-conscious habits during extended study sessions. The application cycles through reminders for hydration, eye care, medicine intake, breathing exercises, physical movement, and rest.

---

## Motivation

As a student pursuing engineering and technology, it becomes essential not only to understand computational principles but also to ensure that our mental and physical health are cared for during periods of intense study. This dual-purpose project addresses both these needs:

- **Number Theory Toolkit:** Deepen understanding of mathematical concepts, algorithmic thinking, and Python programming with performance evaluations.  
- **Health Reminder App:** Support student wellness with automated, periodic reminders encouraging regular breaks and healthy habits.

---

## Project Goals and Objectives

- Build a comprehensive collection of number theory programs for educational use.  
- Implement clear console-based interactions with inputs and outputs for easy user understanding.  
- Utilize Python's `time` and `tracemalloc` modules to provide insights into algorithm performance.  
- Develop a practical app demonstrating how programming aids real-life behaviors through notifications.  
- Ensure cross-platform compatibility for notifications using the `plyer` library.

---

## Features

### Number Theory Toolkit

- **Coverage:** 34 scripts addressing numerous number theory concepts including:  
  * Prime numbers & primality testing (Trial division, Miller-Rabin)  
  * Factorization methods including Pollard Rho  
  * Divisor count, abundant/deficient numbers  
  * Special sequences: Fibonacci, Lucas, Mersenne primes  
  * Modular arithmetic & Chinese Remainder Theorem  
  * Digital roots, Harshad numbers, and more.

- **Performance Measurement:** Each script outputs runtime and memory usage.  
- **User Interaction:** Prompts for user input and displays results clearly.  
- **Educational Purpose:** Focus on clarity and teaching concepts rather than maximum optimization.

### Health Reminder App

- Cycles through reminders for:  
  * Drinking water  
  * Eye rest  
  * Medicine  
  * Breathing exercises  
  * Walking breaks  
  * Rest

- Uses **plyer** for notifications, which supports Windows, macOS, and Linux.  
- Customizable intervals between reminders via `time.sleep()`.  
- Simple console logs show reminder progress for user information.  

---

## Technologies Used

- Python 3.x  
- Standard Python libraries including `time`, `tracemalloc`, `math`, `random`.  
- Third-party `plyer` package for desktop notifications.

---

## Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  
- Ensure you have `pip` available for package installation.

### Install plyer

The Health Reminder App requires the `plyer` library:

pip install plyer



---

## How to Run

### Running Number Theory Scripts

- Save any number theory program as a `.py` file, e.g., `prime_check.py`.  
- Open terminal or command prompt and navigate to the file's location.  
- Run the script with:

python prime_check.py



- Follow on-screen input prompts and observe computation output and resource usage.

### Running Health Reminder App

- Save the reminder app as `health_reminder_app.py`.  
- Run from terminal:

python health_reminder_app.py



- The program will show desktop notifications at preset intervals.  
- Leave the terminal open or minimize it.  
- Press `Ctrl + C` to stop the program when needed.

---

## Workflow Description

### Number Theory Toolkit Workflow per Program

1. Program starts and initializes timers and memory tracking.  
2. User prompted to input parameters.  
3. Performs mathematical calculation using defined algorithms.  
4. Outputs result to console.  
5. Calculates and displays execution time and memory usage.  
6. Ends execution.

### Health Reminder App Workflow

1. Application startup message printed.  
2. Initializes reminder state variable.  
3. Enters an infinite loop.  
4. Depending on state variable, sends appropriate notification message and logs progress.  
5. Waits for a preset time interval (`time.sleep`).  
6. Advances to the next reminder message or cycles back.  
7. Continues until manually interrupted.

---

## Flowchart (Mermaid)

flowchart TD
Start[Start Health Reminder App]
--> Init[Print start message\nset state = 1]
Init --> Choice{Current reminder state?}

Choice -->|1| W[Water Reminder]
Choice -->|2| E[Eye Rest]
Choice -->|3| M[Medicine Reminder]
Choice -->|4| B[Breathing Exercise]
Choice -->|5| K[Walk Break]
Choice -->|6| R[Rest]

W --> S2[Sleep 2 min]
E --> S3[Sleep 3 min]
M --> S5[Sleep 5 min]
B --> S2
K --> S3
R --> S2

S2 --> Update{State > 6?}
S3 --> Update
S5 --> Update

Update -->|Yes| Reset[Reset state = 1]
Update -->|No| Continue[Continue Loop]

Reset --> Choice
Continue --> Choice


---

## Limitations

- The number theory programs prioritize educational clarity and simplicity; hence performance may degrade with very large inputs.  
- Input validation is minimal; users should input valid integers to prevent errors.  
- Memory statistics are limited to Python’s internal usage (via `tracemalloc`), not full system memory.  
- Desktop notifications may behave differently across operating systems depending on system support and user settings.

---

## Future Enhancements

- Integrate all number theory scripts into a comprehensive, menu-driven application for streamlined usage.  
- Enhance input handling with robust validation and error messages.  
- Implement detailed logging for results and performance data collection.  
- Develop a graphical user interface for both projects, improving accessibility.  
- Enable customization and pause/resume features in the Health Reminder App for greater user control.

---
