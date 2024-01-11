# Functions with outputs

def format_name(fname, lname):
    formated_fname = fname.title()
    formated_lname = lname.title()
    return (f"{formated_fname} {formated_lname}")

formated_name = format_name("TAha", "HussEIN")
print(formated_name)