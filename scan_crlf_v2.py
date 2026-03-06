import os

def find_crlf_files(directory):
    # The exact raw bytes for Carriage Return + Line Feed
    crlf_sequence = b'\r\n' 
    
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        
        # Exclude the .git directory. Git's internal binary objects 
        # might randomly contain the 0D 0A byte sequence, which we don't care about.
        if '.git' in dirs:
            dirs.remove('.git')
            
        for filename in files:
            filepath = os.path.join(root, filename)
            
            try:
                # Open the file in 'rb' (read binary) mode. 
                # This guarantees the OS won't alter line endings during reading.
                with open(filepath, 'rb') as f:
                    content = f.read()
                    
                    if crlf_sequence in content:
                        print(f"CRLF found: {filepath}")
                        
            except Exception as e:
                # Catch permission errors or broken symlinks
                print(f"Error reading {filepath}: {e}")

if __name__ == "__main__":
    # Run the check starting in the current directory
    print("Scanning repository for CRLF sequences...")
    find_crlf_files('.')
    print("Scan complete.")
