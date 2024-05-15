import subprocess

def execute_scripts():
    try:
        # Execute 1
        subprocess.run(["python", "1_download_pdf.py"], check=True)
        
        # Execute 2 after 1
        subprocess.run(["python", "2_pdf_to_img.py"], check=True)
        
        subprocess.run(["python", "3_get_table_out_of_img.py"], check=True)

        subprocess.run(["python", "4_get_rows_in_img.py"], check=True)

        subprocess.run(["python", "5_cloudmersive_img_ocr.py"], check=True)

        subprocess.run(["python", "6_produce_final_json.py"], check=True)

    except subprocess.CalledProcessError as e:
        # Handle errors if any script fails
        print(f"Error: {e}")

if __name__ == "__main__":
    execute_scripts()
