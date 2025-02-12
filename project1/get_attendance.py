import pandas as pd

def get_attendance():
    try:
        # Load the attendance Excel file
        file_path = "Attendance.xlsx"
        df = pd.read_excel(file_path)

        # Calculate attendance percentage
        if "Name" not in df.columns or "Attendance" not in df.columns:
            return "Error: Excel file does not have required columns."

        df["Percentage"] = (df["Attendance"] / df["Total Classes"]) * 100

        # Convert to string format
        result = df.to_string(index=False)
        return result

    except Exception as e:
        return f"Error reading attendance: {str(e)}"

if __name__ == "__main__":
    print(get_attendance())
