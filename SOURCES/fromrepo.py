## ################################################################################## ##
##                                                                                    ##
##                     Copyright (c) 2009-2017 ESSENTIAL KAOS                         ##
##        Essential Kaos Open Source License <https://essentialkaos.com/ekol>         ##
##                                                                                    ##
## ################################################################################## ##

from yum.plugins import TYPE_INTERACTIVE

requires_api_version = '2.1'
plugin_type = (TYPE_INTERACTIVE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    parser.add_option('--from', dest='fromrepo',
                      action='store', default=False,
                      help='Use only specified repository for action')

def postreposetup_hook(conduit):
    opts, args = conduit.getCmdLine()
    if opts.fromrepo:
        repos = conduit.getRepos()
        repos.disableRepo("*")
        repos.enableRepo(opts.fromrepo)
