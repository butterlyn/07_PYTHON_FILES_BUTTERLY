#
# Example file for working with filesystem shell methods
#
import os
import shutil
import datetime
import zipfile


def main():
  # make a duplicate of an existing file
  if os.path.exists("textfile.txt"):
    f_path = os.path.realpath("textfile.txt")
    print(
      "\n",
      f_path)
    f_path_new = f_path + ".bak"
    shutil.copyfile(f_path,f_path_new) # copies file data, no metadata
    shutil.copystat(f_path,f_path_new) # copies file with metadata (e.g. last modification date)
    # Check to see if shutil.copystat copied the modification time metadata
    print(
      "\n",
      os.path.getmtime("textfile.txt"),
      "\n\n",
      datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt")),
      "\n",
      datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt.bak")))
    os.rename("./textfile.txt.bak","./newfile.txt.bak")

    with zipfile.ZipFile("testzipfile.zip","w") as newzip:
      dir_path = os.path.split(os.path.realpath("./textfile.txt"))[0]
      newzip.write("textfile.txt")
    
    shutil.make_archive("testzipfolder","zip",os.path.realpath("./"))
    

if __name__ == "__main__":
  main()