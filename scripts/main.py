import cli

if __name__ == '__main__':
    try:
        cli.parseArgs()
    except KeyboardInterrupt:
        print '\n\nInterrupted execution\n'
