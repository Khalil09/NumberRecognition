import cli

if __name__ == '__main__':
    try:
        adapter = cli.getAdapter()
        adapter.run()
    except KeyboardInterrupt:
        print('\n\nInterrupted execution\n')
