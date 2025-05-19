# Cloud SpendGuard 💸☁️

A beginner-friendly Python tool that estimates monthly AWS cloud costs based on EC2, S3, and Lambda usage. Built as part of my Python learning journey to reinforce logic, modular programming, real-world cloud scenarios, and now with an interactive **colorful UI**!

![Cloud SpendGuard UI](https://github.com/TJtech1210/cloud-cost-estimator/blob/main/pictures/cloud_cost_estimatore%20phase%201%20image.png)

## 🔧 Features

- Calculates EC2, S3, and Lambda monthly costs
- Budget warning if usage exceeds $200
- Modular codebase with reusable functions
- Dual-mode support:
  - **Test mode** for sandboxed environments
  - **Interactive input mode** for real users
- **New UI**: Added a colorful, user-friendly **Tkinter** interface with ASCII text art using **PyFiglet** for a creative touch 🎨

## 🚀 Getting Started

1. **Clone this repo**:
   
   ```bash
   git clone https://github.com/TJtech1210/cloud-cost-estimator.git
   cd cloud-cost-estimator
Choose a Version to Run:

Run the Console Version (Without UI):
If you prefer to run the console version without the UI, use:


python3 'Cloud Cost Estimator - Phase 1.py'
Run the UI Version (With Tkinter UI):
If you'd like to run the version with the colorful Tkinter UI, use:


python3 cloud_cost_estimator_gui.py
Switch between test mode and user input mode:
Both versions allow you to switch between test mode and user input mode:

Test Mode (default for both versions):


- ec2_count, s3_count, lambda_count = get_usage_data_test()
User Input Mode (local only):


- ec2_count, s3_count, lambda_count = get_usage_data()
✅ Requirements
Python 3.6+

For UI Version: Tkinter (optional, install it with pip install pyfiglet for the colorful UI)

📦 Future Additions
Dynamic pricing via AWS Pricing API

Config file input (JSON/YAML)

Web UI or CLI dashboard

Cost breakdown by region and tier

🧠 Why This Exists
This project is part of my path toward cloud and AI engineering. I'm focusing on using Python to automate cloud-related tasks and understand real cloud billing logic. Eventually, this will integrate into a larger AWS resource cleanup tool.

👨‍💻 Author
Created by @TJtech1210

📄 License
