from core.server import handlers_manager

def init():
    from core.report.report_handler import ReportHandler
    handlers_manager.getManager().registerHandler(ReportHandler())

    