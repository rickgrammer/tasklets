import sys
import command_line

def main():
    parsed_args = command_line.parse_args()
    import ipdb; ipdb.set_trace()
    if parsed_args.action == 'create':
        pass
    elif parsed_args.action == 'edit':
        pass
    elif parsed_args.action == 'list':
        pass
    elif parsed_args.action == 'delete':
        pass
    else:
        exit('tasklet: %s is not supported. Actions supported: (create, edit, list, delete)' % action)

if __name__ == "__main__":
    main()
