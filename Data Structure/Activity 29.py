class fruit:
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, fruit deleted.')

obj = fruit()
del obj