# Cloud Cost Estimator - Phase 1 (Python Only)

print("Welcome to the Cloud Cost Estimator!")


# Step 1: Choose between test mode and real user input

# TEST MODE: Use this when running in sandboxed or non-interactive environments
#def get_usage_data_test():
  #ec2_count = 3
  #s3_count = 100
  #lambda_count = 100000
  #return ec2_count, s3_count, lambda_count

# REAL INPUT MODE: Use this when running locally
def get_usage_data():
  ec2_count = int(input("How many EC2 instances are you using? "))
  s3_count = int(input("How much S3 storage (in GB) are you using? "))
  lambda_count = int(input("How many Lambda executions this month? "))
  return ec2_count, s3_count, lambda_count

# 👇 Uncomment one of these depending on where you're running this:
#ec2_count, s3_count, lambda_count = get_usage_data_test()
ec2_count, s3_count, lambda_count = get_usage_data()


# Step 2: Define basic pricing (mock values)
ec2 = 25.00
s3 = 0.02
lambda_price = 0.0002

# Step 3: Calculate monthly total cost
def calculate_cost(ec2_count, s3_count, lambda_count):
  ec2_total = ec2 * ec2_count
  s3_total = s3 * s3_count
  lambda_total = lambda_price * lambda_count
  total_cost = ec2_total + s3_total + lambda_total
  return ec2_total, s3_total, lambda_total, total_cost

ec2_total, s3_total, lambda_total, total_cost = calculate_cost(ec2_count, s3_count, lambda_count)

# Step 4: Create a function to print the summary and budget warning
def print_summary(ec2_total, s3_total, lambda_total, total_cost): 
  print(f"EC2 total cost: ${ec2_total:.2f}")
  print(f"S3 total cost: ${s3_total:.2f}")
  print(f"Lambda total cost: ${lambda_total:.2f}")
  print("-------------------------------")
  print(f"Total monthly cloud cost: ${total_cost:.2f}")
  if total_cost > 200:
    print("Warning: Your cloud cost exceeds your budget!")

# Step 5: Call the print_summary function
print_summary(ec2_total, s3_total, lambda_total, total_cost)
