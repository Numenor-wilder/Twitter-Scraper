import roster
import thread
import mention


def mentioned(config, outfile, username):
    mention.getMentioned(config, outfile, username)


# 通过列表获取用户时间线
def userlistThread(config, raw, manifest):
    roster.makeList(raw, manifest)
    thread.getTweetsbylist(manifest, config)


# 获取单个用户时间线
def userThread(config, username):
    thread.getTweetsbyone(username, config)
