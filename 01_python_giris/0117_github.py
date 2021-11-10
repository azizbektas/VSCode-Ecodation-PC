#region vscode_ile_github_cli
"""
Adım 1 → "git enable" seçili mi?
Manage → Settings → arama: "git enable" → seçili olduğuna emin olalım


Adım 2 → git client kurulu mu?
Source Control → Initialize Repository seçilemiyor ise kurulu değildir. "Install git" diyerek kuralım.
https://git-scm.com/


Adım 3 → Repo oluşturalım
https://github.com/ → Proje ile aynı isimde repo oluşturalım
https://github.com/azizbektas/VSCode-Ecodation-PC.git

Adım 4 → Repoyu bağlamak için VSCode terminal ile aşağadaki komutları tırnaklar olmadan girelim
PS C:\VSCode-Ecodation-PC> git config --global user.email "you@example.com"
PS C:\VSCode-Ecodation-PC> git config --global user.name "Your Name"
doğrulamak için, görmek için
PS C:\VSCode-Ecodation-PC> git config --list

Adım 5 → Başlangıç (eng. initial) ayarı için
PS C:\VSCode-Ecodation-PC> git init
doğrulamak için, görmek için klasör altında .git dizini oluştuğunu görün

Adım 6 → Yapılan değişikliklerin o anki durumunu göremek için
PS C:\VSCode-Ecodation-PC> git status
On branch master: branch anlamı → projenin farklı versionları olabilir. Şuanki versionu master
No commits yet: henüz commit etmedik, git repoya göndermedik

Adım 7 → Commit edeceğimiz dizinleri ekleyelim. 
PS C:\VSCode-Ecodation-PC> git add .
PS C:\VSCode-Ecodation-PC> git status
Dizinler stage'e eklendi. Repoya gitmek üzere hazır. Özetle şimdilik cache'deler. 
Çıkarmak için unstage etmek için "git rm"

    
Adım 8 → Local Repoya gönderelim. Commit'e Bir İsim Ver "011121-1425"
PS C:\VSCode-Ecodation-PC> git commit -m 011121-1425 
Commit'leri görmek için
PS C:\VSCode-Ecodation-PC> git log

Adım 9 → Remote Repoya gönderelim
şuan için remote repo belirlendi mi? Görelim
PS C:\VSCode-Ecodation-PC> git remote -v
PS C:\VSCode-Ecodation-PC> git remote add VSCode-Ecodation-PC https://github.com/azizbektas/VSCode-Ecodation-PC.git
PS C:\VSCode-Ecodation-PC> git remote -v
remove etmek için
PS C:\VSCode-Ecodation-PC> git remove commit VSCode-Ecodation-PC 
Repo'ya push etmek için
PS C:\VSCode-Ecodation-PC> git push VSCode-Ecodation-PC master
yada reject hatası alırsanız, force edebilirsiniz.
PS C:\VSCode-Ecodation-PC> git push VSCode-Ecodation-PC master --force
Bu seçenekten sonra Browser ile Authentication'ı gireceksiniz. UName+Pass

Adım 9 → Sonraki her değişiklikte, şu komutlar yetecek
PS C:\VSCode-Ecodation-PC> git add .
PS C:\VSCode-Ecodation-PC> git commit -m 01112021-1504
PS C:\VSCode-Ecodation-PC> git push VSCode-Ecodation-PC master --force
"""
#endregion


#region vscode_ile_github_gui
"""
Adım 1 → "git enable" seçili mi?
Manage → Settings → arama: "git enable" → seçili olduğuna emin olalım

Adım 2 → git client kurulu mu?
Source Control → Initialize Repository seçilemiyor ise kurulu değildir. "Install git" diyerek kuralım.
https://git-scm.com/

Adım 3 → Repo oluşturalım
https://github.com/ → Proje ile aynı isimde repo oluşturalım
https://github.com/azizbektas/VSCode-Ecodation-PC.git

Adım 4 → Vscode ile repoyu bağlamak için "Add Remote"
View → Comment Palette → arama: "Add Remote" 
Repository Url: "repo url'sini ekle" https://github.com/azizbektas/VSCode-Ecodation-PC.git
Remote Name: "remote ismi ekle" VSCode-Ecodation-PC

Adım 5 → Authenticaion/Authorization işlemi için kalıcı token oluştur.
https://github.com/settings/tokens → Generate New Token

Adım 6 → Authenticaion/Authorization işlemi için Account yöntemi ile geçici token oluştur
Turn on Settings Sync → Turn on → Sign in → Github → Authorized Github → VSCode Aç

Adım 8 → Stage All Changes
Commit etmeden önce değişikliklerin üzerinde sağ tıklayıp stage yapıyoruz

Adım 7 → İlk gönderimde yada değişiklik anında her gönderim için Commit and Push yapılmalı
Views and More Actions → Commit | Yada | Source Control → Commit buton → Commit'e Bir İsim Ver "060321-2330"
Views and More Actions → Push | Yada | Status Bar'daki → Synchronize Changes buton, Login İçin Token Gir 

Adım 8 → Olurda Commit anında terminalde aşağıdaki gibi bir hata alırsanız
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
"C:\Program Files\Git>" dizini altında github bilgilerini sırayla girin
C:\Program Files\Git> git config --global user.email "you@example.com"
C:\Program Files\Git> git config --global user.name "Your Name"
"""
#endregion
