import os, random, shutil, time

startTime = time.time()

source = '/Users/jrkni/AppData/Local/Programs/Python/Python310/VSCodeScriptsIMade/HaloVideoRandomizer/Halo Videos'

os.chdir(source)

source_random = random.choice(os.listdir('/Users/jrkni/AppData/Local/Programs/Python/Python310/VSCodeScriptsIMade/HaloVideoRandomizer/Halo Videos'))
destination = '/Program Files (x86)/Steam/steamapps/common/Halo Infinite/videos'
test_destination = '/Users/jrkni/AppData/Local/Programs/Python/Python310/VSCodeScriptsIMade/HaloVideoRandomizer/testfolder'
renameVar = 'intro.mp4'

os.chdir(destination)
print('Directory changed to '+destination)

def main():
    try:
        for file in os.listdir(destination):
            if file == 'intro.mp4':
                print(file+ ' has been identified and is to be deleted.')
                os.remove(destination+ '/' +file)
                print(file+ ' has been deleted.')
                os.chdir(source)
                print('Directory changed to '+source)
                shutil.copy(source_random, destination)
                print(source_random+ ' has been copied to ' +destination)
                os.chdir(destination)
                print('Directory changed to '+destination)
        
        for file in os.listdir(destination):    
            if file == source_random:
                print(source_random+ ' has been identified.')
                os.rename(file, renameVar)
                print(source_random+ ' has been renamed to intro.')
    except:
        os._exit(0)

main()
endTime = time.time()
print(f'Exection time: {endTime - startTime}')