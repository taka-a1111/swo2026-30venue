"""SWO30万円 商品LP10月修正 初校：公開中の science-web.online/30venue/（swo2026_30venue_ver2.0w）に、
佐藤様の修正指示（SWO30万円LP修正_1026.pptx ①〜104）と 10/26 のナビゲーション追加指示を反映する。
「40万円と同じ文字の大きさ・レイアウト」「40万円プランと同じに」の箇所は、校了した SWO40万円 ver3.2
（taka-a1111/swo2026-40venue の main）の表・CSS をそのまま取り込む。
置換は件数を数え、期待値と違えば止める。
使い方：python3 -I build_swo30_oct.py <土台HTML> <40万円 ver3.2 の index.html> <出力HTML>"""
import sys, re, json

src, ref40, dst = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
t40 = open(ref40, encoding='utf-8').read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'COUNT {c} != {n}: {old[:90]!r}')
    s = s.replace(old, new)


def cut(text, a, b, inclusive_end=False):
    i = text.index(a)
    j = text.index(b, i)
    if inclusive_end:
        j += len(b)
    return text[i:j]


MAIL_HREF = 'mailto:swo-mail@science-web.online?subject=%E3%83%A1%E3%83%BC%E3%83%AB%E7%9B%B8%E8%AB%87%E3%81%8A%E7%94%B3%E8%BE%BC%E3%81%BF'
ZOOM_HREF = 'mailto:swo-zoom@science-web.online?subject=Zoom%E7%9B%B8%E8%AB%87%E3%81%8A%E7%94%B3%E8%BE%BC%E3%81%BF&amp;body=%E3%81%94%E5%B8%8C%E6%9C%9B%E6%97%A5%E6%99%82%EF%BC%88%E7%AC%AC3%E5%B8%8C%E6%9C%9B%E3%81%BE%E3%81%A7%EF%BC%89%EF%BC%9A%0D%0A%0D%0A%E3%81%94%E6%89%80%E5%B1%9E%EF%BC%9A%0D%0A%E3%81%8A%E5%90%8D%E5%89%8D%EF%BC%9A%0D%0A'
OLD_BTN2 = ('<div class="btns two" style="margin-top:26px;">\n'
            f'      <a class="btn btn-contact" href="{MAIL_HREF}">メール相談お申込み</a>\n'
            f'      <a class="btn btn-zoom" href="{ZOOM_HREF}">Zoom相談お申込み</a>\n'
            '    </div>')
BTN3 = ('<div class="btns" style="margin-top:26px;">\n'
        f'      <a class="btn btn-contact" href="{MAIL_HREF}">メールで相談する</a>\n'
        f'      <a class="btn btn-zoom" href="{ZOOM_HREF}">Zoom相談を申し込む</a>\n'
        '      <a class="btn btn-tel" href="tel:050-3538-7006">電話　050-3538-7006<small>（平日10時〜15時）</small></a>\n'
        '    </div>')

# ---- BUILD_TAG ----
rep('<!-- BUILD_TAG: swo2026_30venue_ver2.0w / 2026-08-16 -->',
    '<!-- BUILD_TAG: swo2026_30venue_oct_ver1.0 / 2026-10-26 -->')

# ---- ①-2 ＋ 10/26 追加指示：ナビゲーションを40万円と同じ5項目に（会社案内を削除） ----
rep('<li><a href="#price30">登録フォーム</a></li>', '<li><a href="#price30">プラン内容</a></li>')
rep('      <li><a href="#about">会社案内</a></li>\n', '')

# ---- ①② 見出し ----
rep('<span class="sub">学会・国際会議の開催準備を、もっと簡単に。</span>',
    '<span class="sub">大会ホームページは、そのまま活用</span>')
rep('<span class="kw">参加登録フォーム</span><br><span class="kw">演題登録フォーム</span>',
    '<span class="kw">演題登録・参加登録・カード決済</span>')

# ---- ③④⑤ 価格カード（右側は40万円と同じく区切り線の右に） ----
rep('<div class="p"><span class="p-pre">基本</span><span class="p-num">30</span><span class="p-unit">万円</span></div>\n          <div class="p-tax">（消費税　含みません）</div>',
    '<div class="p"><span class="p-pre">基本料金</span><span class="p-num">30</span><span class="p-unit">万円</span></div>\n          <div class="p-tax">（税別）</div>')
rep('''        <!--<div class="hc-sep" aria-hidden="true"></div>
        <div class="hc-right">
          <div class="n">入稿完了から</div>
          <div class="p"><span class="p-num">3</span><span class="p-unit">週間</span></div>
          <div class="p-tax">で公開！</div>
        </div>-->
        <h2>入稿完了から３週間以内に公開！<br>会費はカード決済にて！</h>
''', '''        <div class="hc-sep" aria-hidden="true"></div>
        <div class="hc-right">
          <p class="hc-msg">入稿完了から3週間以内に公開<br>参加費のカード決済に対応</p>
        </div>
''')

# ---- ⑤-2 画像3枚の差し替え ／ ⑥ 文言 ／ ⑦ ボタン3つ ----
rep('''        <img src="images/laptop.png" alt="ノートPC操作の様子" class="on">
        <img src="images/moderators.png" alt="モデレーターの様子">
        <img src="images/registration.png" alt="参加登録の様子">''',
    '''        <img src="images/consultation.jpg" alt="学会の参加登録フォームについて相談する様子" class="on">
        <img src="images/abstract-entry.jpg" alt="学会の演題登録フォームに要旨を入力する女性">
        <img src="images/card-payment.jpg" alt="スマートフォンで参加登録とカード決済を行う様子">''')
rep('<p>ＣＭＳ、スマートフォン対応、ＳＥＯ、アクセス解析まで対応。<br>学会・大学・研究機関向けのWebサイト・システムを、2007年からサポートしてきました。<br>大会の規模や開催時期が決まっていない段階でもご相談いただけます。</p>\n    ' + OLD_BTN2,
    '<ul class="hero-points">\n        <li>・既存の大会ホームページに登録フォームを導入</li>\n        <li>・演題・参加登録の条件に合わせて項目を設定</li>\n      </ul>\n      <p class="hero-note">大会の規模や開催時期が決まっていなくても、ご相談いただけます。</p>\n    ' + BTN3.replace('margin-top:26px', 'margin-top:20px'))

# ---- ⑧⑨⑩ プランの見出し ----
rep('<h2 class="sec-ttl">すぐに使える登録受付フォーム</h2>', '<h2 class="sec-ttl" id="sec-price30">30万円プランに含まれる内容</h2>')
rep('''    <p>必要な登録条件をまとめて 学会・大会に必要な「演題登録」と「参加登録」を一つのシステムにまとめます。
大会の募集要項や運営方法に合わせ、必要な項目を整理します。</p>''',
    '''    <ul class="plan-points">
      <li>・演題登録システム</li>
      <li>・参加登録システム</li>
      <li>・カード決済システム</li>
    </ul>''')
rep('<h2>必要な開催案内を、まとめて制作・準備します</h2>', '<h2 class="plan-lead">大会の募集要項に合わせて、登録項目を設定します。</h2>')

# ---- ⑪〜⑱ 演題登録 ----
rep('<div class="spec-title">演題登録フォーム</div>', '<div class="spec-title">演題登録システム</div>')
rep('''          <tr><td>・発表者名、所属、連絡先</td></tr>
          <tr><td>・共著者・共同研究者情報</td></tr>
          <tr><td>・演題名、発表分野</td></tr>
          <tr><td>・カテゴリー</td></tr>
          <tr><td>・抄録</td></tr>
          <tr><td>・アブストラクト</td></tr>
          <tr><td>・発表形式 オーラル・ポスター</td></tr>
          <tr><td>・キーワード、関連分野</td></tr>
          <tr><td>・確認</td></tr>
          <tr><td>・同意事項</td></tr>
          <tr><td>・登録内容の確認、修正、受付完了通知 など。</td></tr>''',
    '''          <tr><td>発表者・共著者の氏名、所属、連絡先</td></tr>
          <tr><td>演題名、発表分野・カテゴリー、キーワード</td></tr>
          <tr><td>抄録・アブストラクトのアップロード</td></tr>
          <tr><td>発表形式の選択（口頭・ポスター）</td></tr>
          <tr><td>登録内容の確認・修正、受付完了通知</td></tr>
          <tr><td>演題登録マイページ・管理者画面</td></tr>''')

# ---- ⑲〜26 参加登録 ----
rep('<div class="spec-title">参加登録フォーム</div>', '<div class="spec-title">参加登録システム</div>')
rep('''          <tr><td>・早期登録 普通登録 カード決済</td></tr>
          <tr><td>・基本 参加者名、所属、連絡先</td></tr>
          <tr><td>・区分 一般、学生、会員、非会員など</td></tr>
          <tr><td>・種類 講演者 出席者 座長 委員</td></tr>
          <tr><td>・有無 同行者</td></tr>
          <tr><td>・出席 懇親会 出席 食事制限</td></tr>
          <tr><td>・出席 市内見学</td></tr>
          <tr><td>・会費 会員・学生・一般・同行者</td></tr>
          <tr><td>・書類 領収証・出席確認証・ネームカード</td></tr>
          <tr><td>・確認 登録内容。修正、受付完了通知</td></tr>
          <tr><td>・徴収 カード VISA・MASTER・JCB対応</td></tr>
          <tr><td>・登録 マイページ・管理者画面</td></tr>''',
    '''          <tr><td>早期・普通登録、参加区分別の料金設定</td></tr>
          <tr><td>同行者・懇親会・見学の登録、食事制限の確認</td></tr>
          <tr><td>カード決済（Visa・Mastercard・JCBなど）</td></tr>
          <tr><td>領収書・参加証明書・ネームカード</td></tr>
          <tr><td>登録内容の確認・修正、受付完了通知</td></tr>
          <tr><td>参加登録マイページ・管理者画面</td></tr>''')

# ---- 27・28 ----
rep('<li>段階認証、CMS、スマートフォン対応、SEO、アクセス解析など。</li>', '<li>2段階認証・スマートフォン対応</li>')
rep('<li>「募集要項」「開催案内」を確認して必要な項目を整理しましょう。</li>', '<li>募集要項・開催案内をもとに、必要な登録項目を設定します。</li>')

# ---- 29 プレミアムプランへの導線（40万円の「スタンダードプラン 30万円」の枠と同じ中央ぞろえ） ----
rep('''      <span class="bl-name">開催サイトも含めた一式をご検討なら　　　</span>
      <span class="bl-price">プレミアムプラン</span>
      <span class="bl-price">40万円　　　</span>''',
    '''      <span class="bl-name">開催案内ホームページの制作もご希望の方へ</span>
      <span class="bl-plan"><span class="bl-price">プレミアムプラン</span><span class="bl-price">40万円</span></span>''')

# ---- 30・31 ----
rep('<h2>30万円プランについて相談する</h2>', '<h2 class="plan-lead">必要な登録システムを、開発・準備します</h2>')
rep('''    <ul class="worries">
      <li>入稿完了から、３週間以内に公開します。</li>
      <li>「開催日が近い」</li>
      <li>「登録受付を早く始めたい」</li>
      <li>「担当者だけでは準備が進まない」</li>
      <li>「Google・Word Pressにて作りかけたけど」</li>
    </ul>

''', '')

# ---- 32・33 ----
rep('<p class="answer-ttl">そこで、入稿完了から３週間以内の公開を基本としています。</p>',
    '<p class="answer-ttl">入稿完了から3週間以内に公開</p>')

# ---- 34〜39・72〜77 書類ボタン（2か所） ----
rep('<button class="btn btn-quote" data-open="m-basic">基本見積書<br>ダウンロード<small>その場で作成・印刷</small></button>',
    '<button class="btn btn-quote" data-open="m-basic">基本見積書をダウンロード<small>PDF保存・印刷に対応</small></button>', 2)
rep('<button class="btn btn-quote2" data-open="m-ref">最適見積書<br>ダウンロード<small>希望項目を含めて計算</small></button>',
    '<button class="btn btn-quote2" data-open="m-ref">最適見積書をダウンロード<small>ご希望に応じた見積金額を確認できます</small></button>', 2)
rep('<button class="btn btn-order" data-open="m-order">仕様書・発注書・請書<small>入力してそのまま送信</small></button>',
    '<button class="btn btn-order" data-open="m-order">発注書<small>必要事項を入力して送信できます</small></button>', 2)

# ---- 40 削除 ／ 42 見出し ----
rep('''    <h2 class="sec-ttl" id="sec-faq">実績　Ｆ.Ａ.Ｑ.</h2>
    <p>学会・研究分野に特化し、研究者・大学・学会・国際シンポジウムを支援してきた30年間の経験を活かします。</p>

    <h3 class="sub-ttl">よくある大会準備の悩み</h3>
    <ul class="worries">
      <li>・登録フォームを作る方法がわからない</li>
      <li>・システム準備が難しい</li>
      <li>・前任者のWebサイトを引き継げない</li>
      <li>・開催まで時間がない</li>
    </ul>
    <p>サイエンスウェブは「誰でも引き継げる」「更新できる」「早く使える」Webシステムを提供します。</p>

    <h3 class="sub-ttl">Ｆ.Ａ.Ｑ.</h3>''', '''    <h3 class="sub-ttl faq-ttl" id="sec-faq">よくあるご質問</h3>''')

# ---- 43〜52 FAQ ----
FAQ = [
    ('ホームページはあります。登録システムだけ依頼できますか？',
     'はい。既存の大会ホームページを活用し、演題登録・参加登録・カード決済システムを導入できます。'),
    ('30万円プランで対応できるか相談できますか？',
     'はい。30万円プランで対応できる内容をご案内します。<br>ご希望の登録項目や機能を伺い、追加費用がかかる場合は、その内容と金額をお知らせします。'),
    ('登録受付の開始に間に合いますか？',
     '入稿完了から3週間以内の公開が目安です。<br>ご希望の受付開始日を伺い、間に合うように準備を進めるためのスケジュールをご案内します。'),
    ('システムに詳しい担当者がいなくても依頼できますか？',
     'はい。必要な登録項目の整理から、公開後の運用までご相談いただけます。<br>Zoomでも、操作方法や運用の進め方をご案内します。'),
    ('参加者からの問い合わせ対応も依頼できますか？',
     'はい。別途契約のオンライン事務局で対応が可能です。<br>ご希望の作業をお知らせください。対応範囲と費用をご案内します。'),
]
rep('''    <dl class="qa">
      <dt>「参加登録受付」と「演題登録受付」だけお願いできますか？</dt>
      <dd>もちろんです。必要な機能を確認し、30万円プランで対応できる内容をご相談します。</dd>
      <dt>30万円で足りるかわかりません。</dt>
      <dd>大会の内容をお聞かせいただき、必要な予算と構成を整理します。</dd>
      <dt>すぐに公開できますか？</dt>
      <dd>入稿完了から３週間以内の公開を基本としています。</dd>
      <dt>Webに詳しい担当者がいません。</dt>
      <dd>公開後の運用もZoomでご相談します。</dd>
    </dl>''', '    <dl class="qa">\n' + ''.join(f'      <dt>{q}</dt>\n      <dd>{a}</dd>\n' for q, a in FAQ) + '    </dl>')

# FAQ の構造化データも表示内容に合わせる
m = re.search(r'(<script type="application/ld\+json">\s*)(\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?\n\})(\s*</script>)', s, re.S)
if not m:
    sys.exit('FAQ JSON-LD not found')
ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace('<br>', '')}} for q, a in FAQ]}
s = s[:m.start(2)] + json.dumps(ld, ensure_ascii=False, indent=2) + s[m.end(2):]

# ---- 53・93 ボタン3つ（FAQ下・業務内容下） ----
rep(OLD_BTN2, BTN3, 2)

# ---- 54〜62 実績の数字（40万円と同じ） ----
rep('<p class="sec-desc">1997年から国際シンポジウムと学会開催を支援。研究者をサポートしています。</p>',
    '<p class="sec-desc works-desc">1997年から、国際シンポジウムや学会の開催を支援しています。</p>')
rep('<div class="st-num">30<span>件以上</span></div>\n        <div class="st-lbl">年間の学会開催実績</div>',
    '<div class="st-num"><span class="st-pre">年間</span>30<span>件以上</span></div>\n        <div class="st-lbl">学会開催を支援</div>')
rep('<div class="st-num">3<span>週間</span></div>\n        <div class="st-lbl">入稿完了から公開まで</div>',
    '<div class="st-num">130<span>機関</span></div>\n        <div class="st-lbl">大学・研究機関での導入実績</div>')

# ---- 63 実績表（40万円 ver3.2 の表をそのまま取り込む） ----
works40 = cut(t40, '    <!-- 支援実績テーブル', '    <!--<h3 class="sub-ttl">直近の学会開催</h3>')
for w, n in [('<tr class="wk-group">', 5), ('href=', 0), ('PhotoIUPAC2028', 2)]:
    if works40.count(w) != n:
        sys.exit(f'40万円の実績表が想定と違う: {w} {works40.count(w)}')
a = s.index('    <!-- 開催実績テーブル -->')
b = s.index('    <!--<h3 class="sub-ttl">直近の学会開催</h3>')
s = s[:a] + works40 + s[b:]

# ---- 64〜71 ご相談（40万円と同じ3枚のカード） ----
rep('<h2 class="sec-ttl" id="sec-contact">ご相談ください </h2>', '<h2 class="sec-ttl" id="sec-contact">まずは、開催概要をお聞かせください</h2>')
a = s.index('    <div class="talk-grid">', s.index('id="sec-contact"'))
b = s.index('    <div class="btns" style="margin-top:26px;">', a)
old_talk = s[a:b]
for w in ['30万円で何ができるか、まず確認してください', '「参加登録と演題登録だけお願いしたい」', 'お教えください', 'まずはお聞かせください']:
    if old_talk.count(w) != 1:
        sys.exit(f'ご相談カードが想定と違う: {w}')
s = s[:a] + '''    <div class="talk-grid">
      <div class="talk-card">
        <div class="tc-ttl">分かる範囲でお知らせください。</div>
        <p>・学会・大会名、開催時期、開催都市<br>・参加予定人数、ご希望の登録機能</p>
      </div>
      <div class="talk-card">
        <div class="tc-ttl">ご相談ください</div>
        <p>お困りごとやご不安な点、現在の準備状況、前回開催時の課題をご相談ください。</p>
      </div>
      <div class="talk-card">
        <div class="tc-ttl">お任せください</div>
        <p>予算案の作成、海外からの招へい、懇親会の会場予約、協賛金の募集など</p>
      </div>
    </div>
''' + s[b:]

# ---- 78〜92 業務内容（40万円 ver3.2 の表をそのまま取り込む） ----
biz40 = cut(t40, '<table class="tbl-clear biz-tbl">', '</table>', inclusive_end=True)
for w, n in [('<tbody class="biz-group">', 3), ('jimu-system/', 2), ('online-secretariat/', 2), ('30venue', 2)]:
    if biz40.count(w) != n:
        sys.exit(f'40万円の業務内容の表が想定と違う: {w} {biz40.count(w)}')
a = s.index('<table class="tbl-clear">')
b = s.index('</table>', a) + len('</table>')
old_biz = s[a:b]
for w, n in [('tokyo/jimu/', 2), ('<tr>', 11)]:
    if old_biz.count(w) != n:
        sys.exit(f'30万円の業務内容の表が想定と違う: {w} {old_biz.count(w)}')
s = s[:a] + biz40 + s[b:]

# ---- 103 電話受付時間（フッター／書類内も同じ事実なのでそろえる） ・104 ----
rep('<a href="tel:050-3538-7006">050-3538-7006</a>（平日10時〜16時）', '<a href="tel:050-3538-7006">050-3538-7006</a>（平日10時〜15時）')
rep("+'（平日10時〜16時）", "+'（平日10時〜15時）", 2)
rep('<p class="ft-copy">＠SWC　Science Web Corp.</p>', '<p class="ft-copy">＠SWO　Science Web Corp.</p>')

# ---- 「40万円と同じ文字の大きさ・レイアウト」：佐々木様が40万円に入れた体裁をそろえる ----
rep('.hd-logo-img{height:30px;width:auto;display:block;}', '.hd-logo-img{height:50px;width:auto;display:block;}')
rep('section{padding:92px 0;}', 'section{padding:15px 0;}')
rep('  .hero-card{flex-direction:column;align-items:flex-start;gap:16px;padding:22px 24px;}',
    '  .hero-card{flex-direction:column;align-items:center;gap:16px;padding:26px 24px;}')
rep('  letter-spacing:.14em;margin-bottom:20px;', '  letter-spacing:.14em;margin-bottom:10px;')
rep('  padding:32px 40px;gap:0;', '  padding:32px 20px;gap:0;')
rep('''/* 右側「３週間」は控えめに */
.hero-card .hc-right{flex:0 0 auto;padding-left:36px;}
.hero-card .hc-left{flex:1 1 auto;}''', '''/* 区切り線で左右を均等に分け、それぞれの枠内で中央揃え（40万円と同じ） */
.hero-card .hc-left{flex:1 1 0;min-width:0;padding-right:32px;text-align:center;}
.hero-card .hc-right{flex:1 1 0;min-width:0;padding-left:32px;text-align:center;}
.hero-card .hc-left .p,.hero-card .hc-right .p{justify-content:center;}
@media(max-width:700px){.hero-card .hc-left,.hero-card .hc-right{flex:0 0 auto;text-align:center;padding-left:0;padding-right:0;width:100%;}
  .hero-card .hc-left .p,.hero-card .hc-right .p{justify-content:center;}
  .hero-card .hc-sep{margin:18px 0;}
  .hero-card .hc-right{padding-top:15px;padding-bottom:0;}}''')
rep('.talk-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}', '.talk-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}')

# 40万円 ver3.2 の10月修正CSSのうち、30万円にも使う部分（実績表・業務内容の表・中央ぞろえの枠・電話ボタン）
css40 = cut(t40, '/* ===== 10月修正（2026-10）：ここから ===== */', '/* ===== 10月修正 三校：ここまで ===== */', inclusive_end=True)
keep = []
for blk_start, blk_end in [
    ('/* ⑥ 電話ボタン */', '/* ⑫ ⑬ 青枠を大きく、文字も大きく */'),
    ('/* 66〜74 実績の数字・説明を約1.2倍 */', '/* 104 フッターの黒い文字を白に */'),
]:
    keep.append(cut(css40, blk_start, blk_end))
mob = cut(css40, '@media (max-width:760px){\n  .hero h1 .sub{font-size:20px;}', '}\n/* ===== 10月修正：ここまで ===== */')
mob_lines = [l for l in mob.split('\n') if ('st-num' in l or 'works-tbl' in l)]
keep.append('@media (max-width:760px){\n' + '\n'.join(mob_lines) + '\n}\n')
keep.append(cut(css40, '/* 1枚目：30万円の枠を中央ぞろえ */', '/* ===== 10月修正 再校：ここまで ===== */').replace('30万円の枠', 'プレミアムプランの枠'))
keep.append(cut(css40, '/* 業務内容：業務と料金をそろえた表（区分は左ぞろえ、金額は右ぞろえ） */', '/* ===== 10月修正 三校：ここまで ===== */'))

CSS = '''
/* ===== 10月修正（2026-10）：ここから ===== */
/* 40万円と同じ文字の大きさ：見出し・価格カード */
.hero h1 .sub{font-size:28px;letter-spacing:.06em;line-height:1.5;}
.hero-card .n,.hero-card .hc-right .n{font-size:24px;letter-spacing:.08em;}
.hero-card .p-pre{font-size:26px;}
.hero-card .p-unit{font-size:34px;}
.hero-card .p-tax{font-size:14px;margin-top:8px;}
/* ⑤ 価格カードの右側（区切り線の右） */
.hero-card .hc-right{display:flex;align-items:center;justify-content:center;}
.hero-card .hc-msg{margin:0;font-size:24px;font-weight:800;line-height:1.7;letter-spacing:.04em;color:#fff;}
/* ⑤-2 スライドショー：支給画像（1672×941）が切れない比率 */
.media-slot{aspect-ratio:1672/941;}
@media (max-width:760px){ .media-slot{aspect-ratio:1672/941;} }
/* ⑥ 1・2行目は1.5倍、3行目は2倍 */
.hero-points{list-style:none;margin:22px 0 0;padding:0;}
.hero-points li{font-size:24px;font-weight:700;line-height:1.7;color:var(--navy-ink);}
.hero-note{font-size:32px;font-weight:800;line-height:1.5;margin:10px 0 0;color:var(--navy-ink);}
/* ⑨ 30万円プランに含まれる内容 */
.plan-points{list-style:none;margin:6px 0 0;padding:0;}
.plan-points li{font-size:18px;font-weight:700;line-height:1.9;}
.plan-lead{font-size:22px;font-weight:900;color:var(--navy-ink);margin:26px 0 14px;line-height:1.5;}
/* 32・33 1.2倍、同じ大きさ */
.answer-box .answer-ttl{font-size:24px;}
.answer-box .answer-sub{font-size:24px;font-weight:700;line-height:1.6;}
''' + ''.join(keep) + '''@media (max-width:760px){
  .hero h1 .sub{font-size:20px;}
  .hero-card .n,.hero-card .hc-right .n{font-size:20px;}
  .hero-card .p-num{font-size:76px;}
  .hero-card .p-pre{font-size:22px;}
  .hero-card .p-unit{font-size:28px;}
  .hero-card .hc-msg{font-size:19px;}
  .hero-points li{font-size:17px;}
  .hero-note{font-size:21px;}
  .plan-lead{font-size:19px;}
  .answer-box .answer-ttl,.answer-box .answer-sub{font-size:19px;}
}
/* ===== 10月修正：ここまで ===== */
'''
rep('</style>', CSS + '</style>')

open(dst, 'w', encoding='utf-8').write(s)
print('OK', len(s))
