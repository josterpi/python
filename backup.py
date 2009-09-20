
import datetime

# Backup Policy:
# On the first ____ of each month, do a monthly backup, rotating n months
#     yyyy-mm-dd-monthly.tar.gz
# Every _____, do a weekly backup, rotating m months
#     yyyy-mm-dd-weekly.tar.gz
# Daily backups, rotating p days
#     yyyy-mm-dd-daily.tar.gz


class Backup:
    MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY = 0,1,2,3,4,5,6
    MONTH_FORMAT = '%Y-%b-%d-monthly.tar.gz'
    WEEK_FORMAT = '%Y-%b-%d-weekly.tar.gz'
    DAY_FORMAT = '%Y-%b-%d-daily.tar.gz'
    def __init__(self, day_for_monthly, day_for_weekly):
        pass

    def old_monthly(self, months_ago, day_for_backup):
        month_ago_today = self.today - datetime.timedelta(4*7*months_ago)
        first_of_month = datetime.date(month_ago_today.year,
                                       month_ago_today.month,
                                       1)
        while first_of_month.weekday != day_for_backup:
            first_of_month += datetime.timedelta(1)
        return first_of_month.strftime(MONTH_FORMAT)

    def old_weekly(self, weeks_ago, day_for_backup):
        week_ago_today = self.today - datetime.timedelta(7*weeks_ago)
        day_of_week = datetime.date(month_ago_today.year,
                                       month_ago_today.month,
                                       1)
        while first_of_month.weekday != day_for_backup:
            first_of_month += datetime.timedelta(1)
        return first_of_month.strftime(MONTH_FORMAT)
        
    def should_monthly_backup(today, day_for_backup):
        if today.weekday() == day_for_backup and today.day <= day_for_backup:
            return True
        else:
            return False

    def should_weekly_backup(today, day_for_backup):
        if today.weekday() == day_for_backup:
            return True
        else:
            return False


