import cli
import readfiles

if __name__ == '__main__':
    try:
        readfiles.openTesting()
        readfiles.openTraining()
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
