
__all__ = ["dataset_parser"]

import glob, traceback, os, argparse, re
from loguru import logger
from rich_argparse import RichHelpFormatter
from dorothy.dataset import download


class dataset_parser:

  def __init__(self, args):

      # Create Task
      download_parser   = argparse.ArgumentParser(description = '', add_help = False)
  
      download_parser.add_argument('--tag', '-t', action='store', dest='tag', type=str,
                          required=True ,
                          help = "the dataset tag")
      download_parser.add_argument('--output', '-o',action='store', dest='output', type=str,
                          required=False , default=os.getcwd(),
                          help = "the dataset output path.")
      download_parser.add_argument('--token', '-k',action='store', dest='token', type=str,
                          required=False , default=os.environ.get("DOROTHY_TOKEN",""),
                          help = "the token.")
                    

      parent    = argparse.ArgumentParser(description = '', add_help = False)
      subparser = parent.add_subparsers(dest='option')

      # Datasets
      subparser.add_parser('download', parents=[download_parser], formatter_class=RichHelpFormatter)
      args.add_parser( 'dataset', parents=[parent] , formatter_class=RichHelpFormatter)




  def parser( self, args ):

    if args.mode == 'dataset':
      if args.option == 'download':
        self.download(args)
      else:
        logger.error("Option not available.")


  def download(self,args):
    download( args.tag, args.output, token=args.token)

    







