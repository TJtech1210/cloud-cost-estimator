# Cloud Cost Estimator 💸☁️

A beginner-friendly Python tool that estimates monthly AWS cloud costs based on EC2, S3, and Lambda usage. Built as part of my Python learning journey to reinforce logic, modular programming, and real-world cloud scenarios.

## 🔧 Features

- Calculates EC2, S3, and Lambda monthly costs
- Budget warning if usage exceeds $200
- Modular codebase with reusable functions
- Dual-mode support:
  - Test mode for sandboxed environments
  - Interactive input mode for real users

## 🚀 Getting Started

1. Clone this repo:
   
   git clone https://github.com/TJtech1210/cloud-cost-estimator.git
   cd cloud-cost-estimator


2. Run the script:

   'Cloud Cost Estimator - Phase 1.py'
   

3. To switch between test mode and user input:

    Test Mode (default):

     
     ec2_count, s3_count, lambda_count = get_usage_data_test()
     
    User Input Mode (local only):

     
     ec2_count, s3_count, lambda_count = get_usage_data()
     

✅ Requirements

* Python 3.6+
* No external libraries (for now)

📦 Future Additions

* Dynamic pricing via AWS Pricing API
* Config file input (JSON/YAML)
* Web UI or CLI dashboard
* Cost breakdown by region and tier

🧠 Why This Exists

This project is part of my path toward cloud and AI engineering. I'm focusing on using Python to automate cloud-related tasks and understand real cloud billing logic. Eventually, this will integrate into a larger AWS resource cleanup tool.

👨‍💻 Author

Created by [@TJtech1210](https://github.com/TJtech1210)

📄 License

MIT License

