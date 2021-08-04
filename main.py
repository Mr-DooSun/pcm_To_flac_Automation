from load import load_audio
import soundfile as sf

from os import listdir, mkdir
import shutil

if __name__ == '__main__':
    path = ''

    output = ''

    for main_folder in listdir(path) :
        sub_path = path + '/' + main_folder

        try :
            for sub_folder in listdir(sub_path) :
                try :
                    mkdir(output + main_folder)
                except FileExistsError :
                    print('이미 폴더가 만들어져 있습니다. ')

                print(main_folder+'/'+sub_folder)

                sub_sub_folder = path + '/' + main_folder + '/' + sub_folder
            
                file_list = [file for file in listdir(sub_sub_folder) if file.endswith('.pcm')]
                label_list = [file for file in listdir(sub_sub_folder) if file.endswith('.txt')]

                output_path = output + main_folder + '/' + sub_folder

                for file in file_list :
                    try :
                        mkdir(output_path)
                    except FileExistsError :
                        print('이미 폴더가 만들어져 있습니다. ')
                
                    print(sub_sub_folder + '/' + file)
                    audio_pcm = load_audio(sub_sub_folder + '/' + file)
                    # sf.write(output_path + '/' + file[:18] + '.flac', audio_pcm, 16000, format='flac', subtype='PCM_24')
                
                for label in label_list :
                    print(sub_sub_folder + '/' + label)
                    # shutil.copy(sub_sub_folder + '/' + label, output_path + '/' + label)

        except NotADirectoryError :
            print('1번재 경로 폴더가 아님')
        