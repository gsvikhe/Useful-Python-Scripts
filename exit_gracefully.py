def exit_gracefully(signum, frame):

	running = False
	
	original_sigint = signal.getsignal(signal.SIGINT)
	
	signal.signal(signal.SIGINT, original_sigint)
	sys.exit(1)
	signal.signal(signal.SIGINT, exit_gracefully)
