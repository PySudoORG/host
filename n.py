from telethon import TelegramClient , events , Button, sessions
import os,json,subprocess
# ======================= DB ============================ #
if not '/home/yazdancr/.trash/"Anonymous message"/db.json' in os.listdir():
    with open('db.json','w') as x:
        json.dump({'s':'home'},x)
# ======================================================= #
admin = 5263923993
Token = '6481231831:AAEAql1PXZvoHS-9baEy1-EBicvb-78mqiA'
api_id , api_hash = 10179366,'b9f37fae5553298773daf1410d2cb8d0'
orgDIR = '/home/yazdancr/.trash/"Anonymous message"/'
# ======================================================= #
unknown = TelegramClient(sessions.StringSession(),api_id,api_hash).start(bot_token=Token)

@unknown.on(events.NewMessage(chats=admin))
async def Index(event):
    back = [
        [Button.inline('🔙 Back',b'back')]
    ]
    with open(orgDIR+'db.json') as h:
        t = json.load(h)
    diir = '<code>'+str(os.getcwd())+'</code>'
    unknown.parse_mode = 'html'
    if event.raw_text == '/start':
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as k:
            json.dump(t,k)
        panel = [
            [Button.inline('➕ Add section ➕',b'add'),Button.inline('➖ Delete section ➖',b'delete')],
            [Button.inline('♿️ Change dir',b'chdir'),Button.inline('run command 📇',b'RCB')],
            [Button.inline('Get the names of files & folders 📝',b'list')]
        ]
        await event.reply(f'┌┬ [ ⚠️ Panel ⚠️ ]\n│├ Hello welcome to panel 🌹\n│└ Click to a button ☄️\n└──> #{diir}',buttons=panel)
    # ==================== ADD SECTION ================== #
    elif t['s'] == 'UFI':
        try:
            await unknown.send_message(event.sender_id,'♻️ Downloading . . .')
            await unknown.download_media(event.media)
            await event.reply(f'┌ ✅ file {event.media.document.attributes[0].file_name} Uploaded successfully\n└──> #{diir}',buttons=back)
            t['s'] = 'home'
            with open(orgDIR+'db.json','w') as e:
                json.dump(t,e)
        except Exception as u:
            await event.edit(f'┌ ❌ Error : <code>{u}</code>\n└──> #{diir}')
    elif t['s'] == 'UFL':
        os.mkdir(event.raw_text)
        await event.reply(f'┌ ✅ Folder created successfully\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)

    elif t['s'] == 'HFI':
        with open('.'+str(event.raw_text)) as x:
            x.write('@iRLords')
        await event.reply(f'┌ ✅ File created successfully\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)
    elif t['s'] == 'HFL':
        os.mkdir('.'+str(event.raw_text))
        await event.reply(f'┌ ✅ Folder created successfully\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)
    # ==================== ADD SECTION ================== #


    # ==================== DELETE SECTION ================== #
    elif t['s'] == 'DFI':
        try:
            os.remove(str(event.raw_text))
            await event.reply(f'┌ 🟢 file {event.raw_text} deleted successfully\n└──> #{diir}',buttons=back)
            t['s'] = 'home'
            with open(orgDIR+'db.json','w') as e:
                json.dump(t,e)
        except Exception as u:
            await event.reply(f'┌ 🟠 Error : {u}\n└──> #{diir}',buttons=back)
    elif t['s'] == 'DFL':
        try:
            os.rmdir(str(event.raw_text))
            await event.reply(f'┌ 🔷 folder {event.raw_text} deleted successfully\n└──> #{diir}',buttons=back)
            t['s'] = 'home'
            with open(orgDIR+'db.json','w') as e:
                json.dump(t,e)
        except Exception as u:
            await event.reply(f'┌ 🔹 Error : {u}\n└──> #{diir}',buttons=back)
    # ==================== DELETE SECTION ================== #

    # ==================== Change Dir Section ============== #
    elif t['s'] == 'chdir':
        try:
            os.chdir(str(event.raw_text))
            diir = '<code>'+str(os.getcwd())+'</code>'
            await event.reply(f'┌ 🗞 path successfully changed\n└──> #{diir}',buttons=back)
            t['s'] = 'home'
            with open(orgDIR+'db.json','w') as e:
                json.dump(t,e)
        except Exception as u:
            await event.reply(f'┌ 📕 Error : {u}\n└──> #{diir}',buttons=back)
    # ==================== Change Dir Section ============== #

    # ================== COMMAND SECTION ================== #

    elif t['s'] == 'get':
        x = subprocess.getoutput(str(event.raw_text))
        await event.reply(f'┌┬ [ ▶️ ]\n│├ Code : <code>{event.raw_text}</code>\n│└ Output : <code>{x}</code>\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)
    elif t['s'] == 'check':
        code = [str(i) for i in event.raw_text.split()]
        x = subprocess.check_output(code)
        await event.reply(f'┌┬ [ ▶️ ]\n│├ Code : <code>{event.raw_text}</code>\n│└ Output : <code>{x}</code>\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)
    elif t['s'] == 'P':
        code = [str(i) for i in event.raw_text.split()]
        x = subprocess.Popen(code)
        await event.reply(f'┌ 🪛 The code was executed successfully\n└──> #{diir}',buttons=back)
        t['s'] = 'home'
        with open(orgDIR+'db.json','w') as e:
            json.dump(t,e)
    # ================== COMMAND SECTION ================== #


@unknown.on(events.CallbackQuery())
async def Query(event):
    panel = [
        [Button.inline('➕ Add section ➕',b'add'),Button.inline('➖ Delete section ➖',b'delete')],
        [Button.inline('♿️ Change dir',b'chdir'),Button.inline('run command 📇',b'RCB')],
        [Button.inline('Get the names of files & folders 📝',b'list')]
    ]
    back = [
        [Button.inline('🔙 Back',b'back')]
    ]
    with open(orgDIR+'db.json') as x:
        o = json.load(x)
    diir = '<code>'+str(os.getcwd())+'</code>'
    unknown.parse_mode = 'html'
    if event.sender_id == admin:
        # ============= ADD SECTION ============= #
        if event.data == b'add':
            addsec = [
                [Button.inline('📃 Upload a file',b'file'),Button.inline('Add a folder 🗂',b'folder')],
                [Button.inline('👁‍🗨 Create a Hidden file',b'HFI'),Button.inline('Create a Hidden folder 📂',b'HFO')],
                [Button.inline('🔙 Back',b'back')]
            ]
            await event.edit(f'┌┬ [ ➕ Add section ➕ ]\n│└ Click to a button 🔥\n└──> #{diir}',buttons=addsec)
        elif event.data == b'file':
            o['s'] = 'UFI'
            with open(orgDIR+'db.json','w') as b:
                json.dump(o,b)
            await event.edit(f'┌ 🔖 Send me a file to upload\n└──> #{diir}',buttons=back)
        elif event.data == b'folder':
            o['s'] = 'UFL'
            with open(orgDIR+'db.json','w') as r:
                json.dump(o,r)
            await event.edit(f'┌ 🔅 Give me a name to create the folder\n└──> #{diir}',buttons=back)
        
        elif event.data == b'HFI':
            o['s'] = 'HFI'
            with open(orgDIR+'db.json','w') as r:
                json.dump(o,r)
            await event.edit(f'┌ ⚜️ Give me a name to create a hidden file\n└──> #{diir}',buttons=back)

        elif event.data == b'HFL':
            o['s'] = 'HFL'
            with open(orgDIR+'db.json','w') as r:
                json.dump(o,r)
            await event.edit(f'┌ 🔆 Give me a name to create a hidden folder\n└──> #{diir}',buttons=back)
        # ============= ADD SECTION ============= #
        elif event.data == b'back':
            o['s'] = 'home'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌┬ [ ⚠️ Panel ⚠️ ]\n│├ Hello welcome to panel 🌹\n│└ Click to a button ☄️\n└──> #{diir}',buttons=panel)
        # ==================== DELETE SECTION ================== #

        elif event.data == b'delete':
            delete = [
                [Button.inline('❌ Delete a file',b'DFI'),Button.inline('Delete a folder ❌',b'DFL')],
                [Button.inline('🔙 Back',b'back')]
            ]
            await event.edit(f'┌┬ [ ➖ Add section ➖ ]\n│└ Click to a button 🔥\n└──> #{diir}',buttons=delete)
        elif event.data == b'DFI':
            o['s'] = 'DFI'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌ 🔴 Give me a file name to delete it\n└──> #{diir}',buttons=back)
        elif event.data == b'DFL':
            o['s'] = 'DFL'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌ 🔸 Give me a folder name to delete it\n└──> #{diir}',buttons=back)

        # ==================== DELETE SECTION ================== #

        # ==================== Change Dir Section ============== #
        elif event.data == b'chdir':
            chdir = [
                [Button.inline('../',b'/')],
                [Button.inline('🔙 Back',b'back')]
            ]
            o['s'] = 'chdir'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌┬ [ ♦️ Change dir section ♦️ ]\n│├ Enter a path\n│└ Example : /home , /etc , ....\n└──> #{diir}',buttons=chdir)
        elif event.data == b'/':
            os.chdir('../')
            diir = '<code>'+str(os.getcwd())+'</code>'
            await event.edit(f'┌ 🏷 path successfully changed\n└──> #{diir}',buttons=back)
        # ==================== Change Dir Section ============== #

        # ls sec
        elif event.data == b'list':
            i = str()
            for n in os.listdir():
                i += n+'\n'
            if len(i) <= 4096:
                await event.edit(i,buttons=back)
            else:
                await event.edit(f'┌ 📌 caracters is long\n└──> #{diir}',buttons=back)
        # ls sec

        # ================== COMMAND SECTION ================== #
        elif event.data == b'RCB':
            examples = [
                [Button.inline('✏️ getoutput',b'get')],
                [Button.inline('check_output 📯',b'check')],
                [Button.inline('🎊 Popen',b'P')]
            ]
            await event.edit(f'┌┬ [ 🏮 Run Command 🏮 ]\n│└ Choose a example 🪄\n└──> #{diir}',buttons=examples)
        elif event.data == b'get':
            o['s'] = 'get'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌ ⚙️ Give me a code to run\n└──> #{diir}',buttons=back)
        elif event.data == b'check':
            o['s'] = 'check'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌ ⚙️ Give me a code to run\n└──> #{diir}',buttons=back)
        elif event.data == b'P':
            o['s'] = 'P'
            with open(orgDIR+'db.json','w') as y:
                json.dump(o,y)
            await event.edit(f'┌ ⚙️ Give me a code to run\n└──> #{diir}',buttons=back)

        # ================== COMMAND SECTION ================== #

print('API is ON')
unknown.run_until_disconnected()
