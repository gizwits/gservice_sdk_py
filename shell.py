from gservice.client import GServiceClient

if __name__=='__main__':
    gsc = GServiceClient('34bf39829e8b408493cd74298e4427cd')
    try:
        from IPython import embed
        embed()
    except ImportError:
        print "* Warning: you need IPython to run this script!"
