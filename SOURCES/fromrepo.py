## ################################################################################## ##
##                                                                                    ##
##                     Copyright (c) 2009-2017 ESSENTIAL KAOS                         ##
##        Essential Kaos Open Source License <https://essentialkaos.com/ekol>         ##
##                                                                                    ##
## ################################################################################## ##

from yum.plugins import PluginYumExit, TYPE_INTERACTIVE

requires_api_version = '2.1'
plugin_type = (TYPE_INTERACTIVE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    parser.add_option('--repo', dest='fromrepo',
                      action='store', default=False,
                      help='Use only specified repository for action')

def init_hook(conduit):
    parser = conduit.getOptParser()
    opts, args = parser.parse_args()

    if not opts.fromrepo:
        return

    repos = conduit.getRepos()
    allRepos = repos.findRepos('*')

    found = False

    for repo in allRepos:
        if repo.id == opts.fromrepo:
            found = True
            break

    if not found:
        raise PluginYumExit('Repository with name %s does not exist' % opts.fromrepo)

    repos.disableRepo('*')
    repos.enableRepo(opts.fromrepo)
