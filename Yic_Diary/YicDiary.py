from msvcrt import kbhit
import tkinter as tk
import tkinter.ttk as ttk
import datetime as da
import calendar as ca
import pymysql.cursors

WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOUR = ['red', 'black', 'black', 'black','black', 'black', 'blue']
actions = ('学校','試験', '課題', '行事', '就活', 'アルバイト','旅行')

class Login:
    '''ログインを制御するクラス'''

    def connect2(self):
      connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='',
                                    db='apr01',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
      try:
            # トランザクション開始
            connection.begin()

            with connection.cursor() as cursor:
                cursor = connection.cursor()

                sql1 = "select * from family where (last_name, password) = ('{}', '{}');".format(self.name_entry.get(), self.pass_entry.get())
                cursor.execute(sql1)
                tmp = cursor.fetchall()
                if len(tmp) != 0:
                  # 表示中のウィジェットを一旦削除
                  for widget in self.widgets:
                      widget.destroy()

                  # "ログインに成功しました"メッセージを表示
                  self.message = tk.Label(
                      self.master,
                      text="ログインに成功しました",
                      font=("",10)
                  )
                  self.message.place(
                      x=self.master.winfo_width() // 2,
                      y=self.master.winfo_height() // 2,
                      anchor=tk.CENTER
                  )

                  # 少しディレイを入れてredisplayを実行
                  self.master.after(1000, app.destroy)

                else:
                  # 表示中のウィジェットを一旦削除
                  for widget in self.widgets:
                      widget.destroy()

                  # "ログインに失敗しました"メッセージを表示
                  self.message = tk.Label(
                      self.master,
                      text="ログインに失敗しました",
                      font=("",10)
                  )
                  self.message.place(
                      x=self.master.winfo_width() // 2,
                      y=self.master.winfo_height() // 2,
                      anchor=tk.CENTER
                  )

                  # 少しディレイを入れてredisplayを実行
                  self.master.after(1000, self.redisplay)


            connection.commit()

      except Exception as e:
            print('error:', e)
            connection.rollback()
      finally:
            connection.close()




    def __init__(self, master, main):
        '''コンストラクタ
            master:ログイン画面を配置するウィジェット
            body:アプリ本体のクラスのインスタンス
        '''

        self.master = master

        # アプリ本体のクラスのインスタンスをセット
        self.main = main

        # ログイン関連のウィジェットを管理するリスト
        self.widgets = []

        # ログイン画面のウィジェット作成
        self.create_widgets()

    def create_widgets(self):
        '''ウィジェットを作成・配置する'''

        # ユーザー名入力用のウィジェット
        self.name_label = tk.Label(
            self.master,
            text="ユーザー名"
        )
        self.name_label.grid(
            row=0,
            column=0
        )
        self.widgets.append(self.name_label)
        
        global name_entry
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(
            row=0,
            column=1
        )
        self.widgets.append(self.name_entry)

        # パスワード入力用のウィジェット
        self.pass_label = tk.Label(
            self.master,
            text="パスワード"
        )
        self.pass_label.grid(
            row=1,
            column=0
        )
        self.widgets.append(self.pass_label)

        self.pass_entry = tk.Entry(
            self.master,
            show="*"
        )
        self.pass_entry.grid(
            row=1,
            column=1
        )
        self.widgets.append(self.pass_entry)

        # ログインボタン
        self.login_button = tk.Button(
            self.master,
            text="ログイン",
            command=self.connect2
        )
        self.login_button.grid(
            row=2,
            column=0,
            columnspan=2,
        )
        self.widgets.append(self.login_button)

        # 登録ボタン
        self.register_button = tk.Button(
            self.master,
            text="登録",
            command=self.register
        )
        self.register_button.grid(
            row=3,
            column=0,
            columnspan=2,
        )
        self.widgets.append(self.register_button)

        # ウィジェット全てを中央寄せ
        self.master.grid_anchor(tk.CENTER)

        print(self.name_entry.get())
        print(self.pass_entry.get())

    def login(self):
        '''ログインを実行する'''

        # 入力された情報をEntryウィジェットから取得
        username = self.name_entry.get()
        password = self.pass_entry.get()

    def register(self):
        '''ユーザー名とパスワードを登録する'''

        # 入力された情報をEntryウィジェットから取得
        username = self.name_entry.get()
        password = self.pass_entry.get()

        # 表示中のウィジェットを一旦削除
        for widget in self.widgets:
            widget.destroy()

        # "ログインに失敗しました"メッセージを表示
        self.message = tk.Label(
            self.master,
            text="ログインに失敗しました",
            font=("",10)
        )
        self.message.place(
            x=self.master.winfo_width() // 2,
            y=self.master.winfo_height() // 2,
            anchor=tk.CENTER
        )

        # 少しディレイを入れてredisplayを実行
        self.master.after(1000, self.redisplay)

    def redisplay(self):
        '''ログイン画面を再表示する'''

        # "ログインできませんでした"メッセージを削除
        self.message.destroy()

        # ウィジェットを再度作成・配置
        self.create_widgets()

    def success(self):
        '''ログイン成功時の処理を実行する'''

        # 表示中のウィジェットを一旦削除
        for widget in self.widgets:
            widget.destroy()

        # "ログインに成功しました"メッセージを表示
        self.message = tk.Label(
            self.master,
            text="ログインに成功しました",
            font=("",10)
        )
        self.message.place(
            x=self.master.winfo_width() // 2,
            y=self.master.winfo_height() // 2,
            anchor=tk.CENTER
        )

        # 少しディレイを入れてredisplayを実行
        self.master.destroy()

    def main_start(self):
        '''アプリ本体を起動する'''

        # アプリ本体を起動
        self.main.start(self.login_name)
        
class MainAppli:
    '''アプリ本体'''

    def __init__(self, master):
        '''
            コンストラクタ
            master:ログイン画面を配置するウィジェット
        '''

        self.master = master

        # ログイン完了していないのでウィジェットは作成しない

    def start(self, login_name):
        '''アプリを起動する'''

        # ログインユーザー名を表示する
        self.message = tk.Label(
            self.master,
            font=("",10),
            text=login_name + "でログイン中"
        )
        self.message.pack()

        # 必要に応じてウィジェット作成やイベントの設定なども行う


app = tk.Tk()

# メインウィンドウのサイズ設定
app.geometry("300x200")

# アプリ本体のインスタンス生成
main = MainAppli(app)

# ログイン管理クラスのインスタンス生成
login = Login(app, main)


class YicDiary(Login):
  def __init__(self, root):
    root.title('予定管理アプリ')
    root.geometry('520x280')
    root.resizable(0, 0)
    root.grid_columnconfigure((0, 1), weight=1)
    self.sub_win = None

    self.year  = da.date.today().year
    self.mon = da.date.today().month
    self.today = da.date.today().day

    self.title = None
    # 左側のカレンダー部分
    leftFrame = tk.Frame(root)
    leftFrame.grid(row=0, column=0)
    self.leftBuild(leftFrame)

    # 右側の予定管理部分
    rightFrame = tk.Frame(root)
    rightFrame.grid(row=0, column=1)
    self.rightBuild(rightFrame)


#-----------------------------------------------------------------
# アプリの左側の領域を作成する
#
# leftFrame: 左側のフレーム
  def leftBuild(self, leftFrame):
    self.viewLabel = tk.Label(leftFrame, font=('', 10))
    beforButton = tk.Button(leftFrame, text='＜', font=('', 10), command=lambda:self.disp(-1))
    nextButton = tk.Button(leftFrame, text='＞', font=('', 10), command=lambda:self.disp(1))

    self.viewLabel.grid(row=0, column=1, pady=10, padx=10)
    beforButton.grid(row=0, column=0, pady=10, padx=10)
    nextButton.grid(row=0, column=2, pady=10, padx=10)

    self.calendar = tk.Frame(leftFrame)
    self.calendar.grid(row=1, column=0, columnspan=3)
    self.disp(0)


#-----------------------------------------------------------------
# アプリの右側の領域を作成する
#
# rightFrame: 右側のフレーム
  def rightBuild(self, rightFrame):
    self.r1_frame = tk.Frame(rightFrame)
    self.r1_frame.grid(row=0, column=0, pady=10)

    temp = '{}年{}月{}日の予定'.format(self.year, self.mon, self.today)
    self.title = tk.Label(self.r1_frame, text=temp, font=('', 12))
    self.title.grid(row=0, column=0, padx=20)

    button = tk.Button(rightFrame, text='追加', command=lambda:self.add())
    button.grid(row=0, column=1)

    self.r2_frame = tk.Frame(rightFrame)
    self.r2_frame.grid(row=1, column=0)

    self.schedule()


#-----------------------------------------------------------------
# アプリの右側の領域に予定を表示する
#
  def schedule(self):
    # ウィジットを廃棄
    for widget in self.r2_frame.winfo_children():
      widget.destroy()

    self.text = tk.Text(self.r2_frame, width=30, height=10)
    self.text.grid(row=1, column=1)
    scroll_v = tk.Scrollbar(self.r2_frame, orient=tk.VERTICAL, command=self.text.yview)
    scroll_v.grid(row=1, column=2, sticky=tk.N+tk.S)
    self.text["yscrollcommand"] = scroll_v.set


    # データベースに予定の問い合わせを行う
    #lbl = tk.Label()
    #lbl.place(x=30, y=70)

#-----------------------------------------------------------------
# カレンダーを表示する
#
# argv: -1 = 前月
#        0 = 今月（起動時のみ）
#        1 = 次月
  def disp(self, argv):
    self.mon = self.mon + argv
    if self.mon < 1:
      self.mon, self.year = 12, self.year - 1
    elif self.mon > 12:
      self.mon, self.year = 1, self.year + 1

    self.viewLabel['text'] = '{}年{}月'.format(self.year, self.mon)

    cal = ca.Calendar(firstweekday=6)
    cal = cal.monthdayscalendar(self.year, self.mon)

    # ウィジットを廃棄
    for widget in self.calendar.winfo_children():
      widget.destroy()

    # 見出し行
    r = 0
    for i, x in enumerate(WEEK):
      label_day = tk.Label(self.calendar, text=x, font=('', 10), width=3, fg=WEEK_COLOUR[i])
      label_day.grid(row=r, column=i, pady=1)

    # カレンダー本体
    r = 1
    for week in cal:
      for i, day in enumerate(week):
        if day == 0: day = ' ' 
        label_day = tk.Label(self.calendar, text=day, font=('', 10), fg=WEEK_COLOUR[i], borderwidth=1)
        if (da.date.today().year, da.date.today().month, da.date.today().day) == (self.year, self.mon, day):
          label_day['relief'] = 'solid'
        label_day.bind('<Button-1>', self.click)
        label_day.grid(row=r, column=i, padx=2, pady=1)
      r = r + 1

    # 画面右側の表示を変更
    if self.title is not None:
      self.today = 1
      self.title['text'] = '{}年{}月{}日の予定'.format(self.year, self.mon, self.today)


#-----------------------------------------------------------------
# 予定を追加したときに呼び出されるメソッド
#
  def add(self):
    if self.sub_win == None or not self.sub_win.winfo_exists():
      self.sub_win = tk.Toplevel()
      self.sub_win.geometry("300x300")
      self.sub_win.resizable(0, 0)

      # ラベル
      sb1_frame = tk.Frame(self.sub_win)
      sb1_frame.grid(row=0, column=0)
      temp = '{}年{}月{}日　追加する予定'.format(self.year, self.mon, self.today)
      title = tk.Label(sb1_frame, text=temp, font=('', 12))
      title.grid(row=0, column=0)

      # 予定種別（コンボボックス）
      sb2_frame = tk.Frame(self.sub_win)
      sb2_frame.grid(row=1, column=0)
      label_1 = tk.Label(sb2_frame, text='種別 : 　', font=('', 10))
      label_1.grid(row=0, column=0, sticky=tk.W)
      self.combo = ttk.Combobox(sb2_frame, state='readonly', values=actions)
      self.combo.current(0)
      self.combo.grid(row=0, column=1)

      # 家族関係
      '''
      self.label_2 = tk.Label(sb2_frame, text='関係 :', font=('', 10))
      self.label_2.grid(row=0, column=4)

      self.relation = tk.Label(sb2_frame, text=self.login_info(), width=5)
      self.relation.grid(row=0, column=5)
      '''
      '''
      label_2 = tk.Label(sb2_frame, text='関係 :')
      label_2.grid(row=0, column=2)
      self.label_3 = tk.Label(sb2_frame, text=self.connect())
      self.label_3.grid(row=0, column=3)
      '''

      # テキストエリア（垂直スクロール付）
      sb3_frame = tk.Frame(self.sub_win)
      sb3_frame.grid(row=2, column=0)
      self.text = tk.Text(sb3_frame, width=40, height=15)
      self.text.grid(row=0, column=0)
      scroll_v = tk.Scrollbar(sb3_frame, orient=tk.VERTICAL, command=self.text.yview)
      scroll_v.grid(row=0, column=1, sticky=tk.N+tk.S)
      self.text["yscrollcommand"] = scroll_v.set

      # 保存ボタン
      sb4_frame = tk.Frame(self.sub_win)
      sb4_frame.grid(row=3, column=0, sticky=tk.NE)
      button = tk.Button(sb4_frame, text='保存', command=lambda:self.done())
      button.pack(padx=10, pady=10)
    elif self.sub_win != None and self.sub_win.winfo_exists():
      self.sub_win.lift()

      # 関係を取り出す
  def connect(self):
      connection = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  db='apr01',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
      try:
          # トランザクション開始
          connection.begin()

          with connection.cursor() as cursor:
              cursor = connection.cursor()

              sql100 = "select relation.relation from relation inner join family on relation.relation = family.relation where (last_name, password) = ('{}', '{}');".format(Login().create_widgets())
              cursor.execute(sql100)
              for dict in cursor:
                for key, value in dict.items():
                # if
                # {'relation': '母'}
                #    key     :  value
                  return value
                  #label_3 = tk.Label(sb2_frame, text=value)
                  #label_3.grid(row=0, column=3)


          connection.commit()

      except Exception as e:
          print('error:', e)
          connection.rollback()
      finally:
          connection.close()

      # データベースに新規予定を挿入する


  def insert(self):
      connection = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  db='apr01',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
      try:
          # トランザクション開始
          connection.begin()

          with connection.cursor() as cursor:
              cursor = connection.cursor()

              date = '{}-{}-{}'.format(self.year, self.mon, self.today)
              #relation = self.label_3.cget("text")
              self.category = self.combo.get()
              self.contents = self.text.get("1.0", "end")
              sql100 = "insert into schedule(date, category, contents) values('{}', '{}', '{}');".format(date, self.category, self.contents)
              
              cursor.execute(sql100)
              
                #for dict in cursor:
                #for key, value in dict.items():
                # if
                # {'relation': '母'}
                #    key     :  value
                  #return value
                  #label_3 = tk.Label(sb2_frame, text=value)
                  #label_3.grid(row=0, column=3)
              

          connection.commit()

      except Exception as e:
          print('error:', e)
          connection.rollback()
      finally:
          connection.close()


#-----------------------------------------------------------------
# 予定追加ウィンドウで「保存」を押したときに呼び出されるメソッド
#
  def done(self):
    # 日付
    self.date = '{}-{}-{}'.format(self.year, self.mon, self.today)
    print(self.date)

    # 種別
    category = self.combo.get()
    print(category)

    # 予定詳細
    contents = self.text.get("1.0", "end")
    print(contents)

    self.insert()

    self.sub_win.destroy()

#-----------------------------------------------------------------
# 日付をクリックした際に呼びだされるメソッド（コールバック関数）
#
# event: 左クリックイベント <Button-1>
  def click(self, event):
    self.date = '{}-{}-{}'.format(self.year, self.mon, self.today)

    day = event.widget['text']
    if day != ' ':
      self.title['text'] = '{}年{}月{}日の予定'.format(self.year, self.mon, day)
      self.today = day

    connection = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  db='apr01',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
    try:
        connection.begin()

        with connection.cursor() as cursor:
            cursor = connection.cursor()

            sql10 = "select category,contents from schedule where date='{}';".format(self.date)

            print(sql10)

            cursor.execute(sql10)

            self.schedule()
                       
            for key, value in cursor.fetchall()[0].items():
                if key == 'category':
                    category = value
                    self.text.insert(1.0, f'{key}:{value}\n')
                    #label1 = tk.Label(self.r1_frame, text=category)
                    #label1.grid(row=1, column=0)
                if key == 'contents':
                    contents = value
                    self.text.insert(1.0, f'{key}:{value}\n')
                    #label2 = tk.Label(self.r1_frame, text=contents)
                    #label2.grid(row=2, column=0)
              
    except Exception as e:
        print('error:', e)
        connection.rollback()
    finally:
        connection.close()
    
#--------------------------------------------------------------------------------
# ログイン情報
#
  def login_info(self):
    connection = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='',
                                  db='apr01',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            global name
            name = self.name_entry.get()
            global pass_code
            pass_code = self.password.get()
            cursor.execute("select relation from family where last_name = '{}' and password = '{}';".format(name, pass_code))
            for dict in cursor:
              for key, value in dict.items():
                  return value

    except Exception as e:
      print('ERROR:', e)
      connection.rollback()

    finally:
        connection.close()

def Main():
  app.mainloop()
  root = tk.Tk()
  YicDiary(root)
  root.mainloop()

if __name__ == '__main__':
  Main()

