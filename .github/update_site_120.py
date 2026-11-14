from pathlib import Path
import json,subprocess
REPO='jerkgram/Jerkgram-iOS';TAG='v1.2.0';IPA='Jerkgram-1.2.0.ipa'
SHA='4c520eb3cf8cade914903a1cdc08f54c7b0dc73c8916dbec6361bfe8f76254f1';SIZE=101719687
def api(path):return json.loads(subprocess.check_output(['gh','api',path],text=True))
def write(name,data):Path(name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
r=api('repos/'+REPO+'/releases/tags/'+TAG)
assert not r['draft'] and not r['prerelease'] and r['name']=='Jerkgram 1.2.0'
a={x['name']:x for x in r['assets']};assert set(a)=={IPA,'Jerkgram-1.2.0-source.tar.xz','public-source-manifest.json'}
expected_assets={'Jerkgram-1.2.0-source.tar.xz': {'size': 162460448, 'sha256': '71ee50b4a664a21371ff03a816d9ef3a291b93192b4b99d72b92d482f7566ce5'}, 'public-source-manifest.json': {'size': 13028134, 'sha256': 'd7db2e01f60736d5eb2c06af9cb22b334fdd1043e16397e6fa7c91bff1746809'}, 'Jerkgram-1.2.0.ipa': {'size': 101719687, 'sha256': '4c520eb3cf8cade914903a1cdc08f54c7b0dc73c8916dbec6361bfe8f76254f1'}}
for name,row in expected_assets.items():assert a[name]['size']==row['size'] and a[name]['digest']=='sha256:'+row['sha256']
meta=api('repos/'+REPO+'/contents/JERKGRAM_RELEASE.json?ref='+TAG)
import base64
meta=json.loads(base64.b64decode(meta['content']))
assert meta['buildNumber']==183 and meta['ipa']['sha256']==SHA
latest=json.loads(Path('latest.json').read_text());old_latest=dict(latest)
latest.update(status='stable',version='1.2.0',build='183',telegramBaseVersion='13.2',minimumIOS='15.0',githubReleaseUrl=r['html_url'],fileName=IPA,downloadUrl=a[IPA]['browser_download_url'],size=SIZE,sha256=SHA,publicSourceTag=TAG,sourceUrl='https://github.com/'+REPO+'/tree/'+TAG,releaseDate=r['published_at'])
alt=json.loads(Path('altstore-source.json').read_text());app=next(x for x in alt['apps'] if x['bundleIdentifier']=='com.jerkgram.ios')
previous=list(app['versions']);assert not any(x.get('buildVersion')=='183' for x in previous)
app['versions'].insert(0,dict(version='13.2',buildVersion='183',marketingVersion='1.2.0',date=r['published_at'],localizedDescription='Jerkgram 1.2.0 Stable. Based on Telegram for iOS 13.2.',downloadURL=a[IPA]['browser_download_url'],size=SIZE,sha256=SHA,minOSVersion='15.0'))
assert app['versions'][1:]==previous
mirrors=json.loads(Path('mirrors.json').read_text());mirrors['canonical'].update(releaseUrl=r['html_url'],downloadUrl=a[IPA]['browser_download_url'],sha256=SHA)
for name,value in [('latest.json',latest),('altstore-source.json',alt),('mirrors.json',mirrors)]:write(name,value)
changed=set(subprocess.check_output(['git','diff','--name-only'],text=True).splitlines());assert changed=={'latest.json','altstore-source.json','mirrors.json'},changed
subprocess.run(['git','diff','--check'],check=True)
Path('.github/workflows/update-site-release-once.yml').unlink();Path('.github/update_site_120.py').unlink()
for args in [('config','user.name','github-actions[bot]'),('config','user.email','41898282+github-actions[bot]@users.noreply.github.com'),('add','-A'),('commit','-m','Publish Jerkgram 1.2.0 website metadata'),('push','origin','HEAD:main')]:subprocess.run(['git',*args],check=True)
print('Updated canonical website/AltStore/SideStore metadata; previous versions preserved.')
