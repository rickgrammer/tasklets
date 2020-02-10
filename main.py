import command_line
import tasklet_handler

def main():
    parsed_args = command_line.parse_args()
    handler = tasklet_handler.TaskletHandler(parsed_args)
    handler.run()

if __name__ == "__main__":
    main()
