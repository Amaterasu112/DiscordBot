def checkAdmin(self, ctx):
    if ctx.author.id in self.admins:
        return True
    else:
        return False
