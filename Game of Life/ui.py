from service import Service

class UI:
    def __init__(self, service):
        self._service = service

    def start(self):
        print(self._service.getBoard())
        while True:
            try:
                #print(self._service.getBoard())
                cmd = input("Enter command: ")
                cmd = cmd.split(' ')
                #print(cmd)
                if cmd[0] == 'place':
                    if len(cmd) != 3:
                        print("Bad command")
                        continue
                    coordinates = cmd[2].split(',')
                    if len(coordinates) != 2:
                        print("Bad command")
                        continue
                    self._service.placePattern(cmd[1], int(coordinates[0]), int(coordinates[1]))
                    print(self._service.getBoard())
                elif cmd[0] == 'tick':
                    
                    if len(cmd) == 1: #default value 1
                        self._service.tick(1)
                    else:
                        if len(cmd) != 2:
                            print("Bad command")
                            continue
                        self._service.tick(int(cmd[1]))

                    print(self._service.getBoard())

                elif cmd[0] == 'save':
                    if len(cmd) != 2:
                        print("Bad command")
                        continue
                    self._service.saveFile(cmd[1])

                elif cmd[0] == 'load':
                    self._service.loadFile(cmd[1])
                    print(self._service.getBoard())

                elif cmd[0] == 'exit':
                    return
                else:
                    print("Bad command")

            except Exception as ex:
                print(ex)
            