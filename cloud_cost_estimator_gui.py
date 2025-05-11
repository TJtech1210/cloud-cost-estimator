import tkinter as tk
from tkinter import messagebox
import pyfiglet

# Step 1: Define function to calculate costs
def calculate_cost():
    try:
        # Get user inputs
        ec2_count = int(entry_ec2.get())
        s3_count = int(entry_s3.get())
        lambda_count = int(entry_lambda.get())
        
        # Define basic pricing (mock values)
        ec2 = 25.00
        s3 = 0.02
        lambda_price = 0.0002

        # Calculate costs
        ec2_total = ec2 * ec2_count
        s3_total = s3 * s3_count
        lambda_total = lambda_price * lambda_count
        total_cost = ec2_total + s3_total + lambda_total

        # Show result in message box
        result = f"EC2 total cost: ${ec2_total:.2f}\nS3 total cost: ${s3_total:.2f}\nLambda total cost: ${lambda_total:.2f}\nTotal monthly cost: ${total_cost:.2f}"

        # Check if the total cost exceeds $200
        if total_cost > 200:
            result += "\n\nWarning: Your cloud cost exceeds your budget!"

        messagebox.showinfo("Cost Summary", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Step 2: Create the main window
root = tk.Tk()
root.title("Cloud Cost Estimator")
root.geometry("400x350")  # Set window size

# Set a colorful background
root.config(bg="#f0f8ff")

# Step 3: Create a fun banner using PyFiglet
banner = pyfiglet.figlet_format("Cloud Cost Estimator", font="slant")
banner_label = tk.Label(root, text=banner, font=("Courier", 10), bg="#f0f8ff", padx=10)
banner_label.pack(pady=10)

# Step 4: Create UI components (Labels, Entry fields, Buttons)
label_ec2 = tk.Label(root, text="How many EC2 instances are you using?", bg="#f0f8ff", font=("Arial", 12))
label_ec2.pack(pady=10)

entry_ec2 = tk.Entry(root, font=("Arial", 12), bg="#e6f7ff")
entry_ec2.pack(pady=5)

label_s3 = tk.Label(root, text="How much S3 storage (in GB) are you using?", bg="#f0f8ff", font=("Arial", 12))
label_s3.pack(pady=10)

entry_s3 = tk.Entry(root, font=("Arial", 12), bg="#e6f7ff")
entry_s3.pack(pady=5)

label_lambda = tk.Label(root, text="How many Lambda executions this month?", bg="#f0f8ff", font=("Arial", 12))
label_lambda.pack(pady=10)

entry_lambda = tk.Entry(root, font=("Arial", 12), bg="#e6f7ff")
entry_lambda.pack(pady=5)

# Step 5: Create a colorful button to trigger the calculation
button_calculate = tk.Button(root, text="Calculate Cost", command=calculate_cost, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
button_calculate.pack(pady=20)

# Step 6: Start the Tkinter event loop
root.mainloop()
