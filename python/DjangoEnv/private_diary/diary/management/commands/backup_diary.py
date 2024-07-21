import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Diary

class Command(BaseCommand):
    help = "Backup diary data"

    def handle(self, *args, **options):
        # 現在日時を取得
        datestr = datetime.date.today().strftime('%Y%m%d')

        # バックアップファイルの保存先ディレクトリを作成
        filename = f"{settings.BACKUP_PATH}diary_{datestr}.csv"

        #ディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # バックアップファイルに書き込み
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # ヘッダを出力
            header = [field.name for field in Diary._meta.fields]
            csvwriter.writerow(header)

            # データを取得し出力
            diaries = Diary.objects.all()

            for diary in diaries:
                csvwriter.writerow([diary.title, diary.content, diary.photo1, diary.photo2, diary.photo3, diary.created_at, diary.updated_at])

        #ファイルリストを取得
        files = os.listdir(f"{settings.BACKUP_PATH}")
        # 古いバックアップファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(f"{settings.BACKUP_PATH}{files[0]}")