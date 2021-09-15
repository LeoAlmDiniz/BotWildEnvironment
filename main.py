from src.Context.WBEContext import WBEContext


def main(resetContext=True):
    ctx = WBEContext(resetContext)
    ctx.run()


if __name__ == '__main__':
    main()
