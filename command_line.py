import argparse

base_subparser_help = "%s tasklets with '%s' command"

create_subparser_help = base_subparser_help % (('create',)*2)
list_subparser_help = base_subparser_help % (('list',)*2)
edit_subparser_help = base_subparser_help % (('edit',)*2)
delete_subparser_help = base_subparser_help % (('delete',)*2)

parser = argparse.ArgumentParser(prog='tasklet')
subparsers = parser.add_subparsers(dest='action',
    help='Use tasklet to create/track your tasks.')

def set_create_parser():
    # Argument parsing: tasklet - create
    create_parser = subparsers.add_parser('create', help=create_subparser_help)
    create_parser.add_argument('-w', '--when', help='Set the date and time for the tasklet.')
    create_parser.add_argument('-n', '--name',
                               help='Give your tasklet a name (make it concise - less than 30 characters long)',
                               required=True
                               )
    create_parser.add_argument(
        '-d', '--description', help='Describe your tasklet (less than 150 characters long))')
    create_parser.add_argument('-p', '--priority', type=int, default=3,
                               help='Set a priority to the tasklet (0-5), 0 being the highest priority')
    create_parser.add_argument('-t', '--tag', default='generic',
                               help='Add a tag to the tasklet (Ex. work, hobby, mundane etc.), helps in grouping the tasklets')

def set_list_parser():
    # Argument parsing: tasklet - read
    list_parser = subparsers.add_parser('list',  help=list_subparser_help)
    list_parser.add_argument('-t', '--tag', help='List the stored tags.')
    list_parser.add_argument('-f', '--find', help='Find a tasklet with name')

def set_edit_parser():
    # Argument parsing: tasklet - edit
    edit_parser = subparsers.add_parser('edit',  help=edit_subparser_help)
    edit_parser.add_argument('-t', '--tag', help='Change the tag.')
    edit_parser.add_argument('-d', '--done', help='Mark the tasklet as done.')
    edit_parser.add_argument('-n', '--name', help='Rename the tasklet')
    edit_parser.add_argument('-p', '--priority', type=int, help='Change the priority.')

def set_delete_parser():
    # Argument parsing: tasklet - delete
    delete_parser = subparsers.add_parser('delete',  help=delete_subparser_help)
    delete_parser.add_argument(
        'id', help='delete tasklet with tasklet-id')
 
def parse_args():
    set_create_parser()
    set_list_parser()
    set_edit_parser()
    set_delete_parser()
    return parser.parse_args()