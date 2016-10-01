set laststatus=2   " всегда показывать строку статуса
set statusline=%f%m%r%h%w\ %y\ enc:%{&enc}\ ff:%{&ff}\ fenc:%{&fenc}%=col:%2c\ line:%2l/%L\ [%2p%%] "формат строки статуса
"комментарий
"%f - имя файла и путь к нему, относительно текущего каталога
"%m - флаг модификации/изменения, выводит [+] если буфер изменялся
"%r - флаг только для чтения, выводит [RO] если буфер только для чтения
"%h - флаг буфера помощи, выводит [help] если буфер со справкой vim
"%w - флаг окна превью, выводит [Preview]
"'\ ' - экранированный символ пробела. Пробел можно указывать только экранированным, иначе ошибка синтаксиса
"%y - тип файла в буфере, например [vim]
"enc:%{&enc} - отображение кодировки encoding (enc). Обратите внимание: enc: - текст, %{&enc} - вывод значения внутренней переменной (enc)
"ff:%{&ff} - отображение формата перевода строки fileformat (ff)
"fenc:%{&fenc} - отображение кодировки сохранения в файл fileencoding (fenc)
"%= - далее выравнивать вправо
"ch:%3b - код символа под курсором в десятичной чистеме счисления, минимум 3 символа
"hex:%2B - код символа под курсором в шестнадцатеричной системе счисления, минимум 2 символа
"col:%2c - курсор в колонке, минимум 2 символа
"line:%2l/%L - курсор в строке (минимум 2 символа)/всего строк в файле
"%2p - число % в строках, где находится курсор (0% - начало файла; 100% - конец файла), минимум 2 символа
"%% - т.к. символ '%' используется для переменных, то вывод символа '%' в строке статуса нужно делать особым образом - %%

"Читать pdf-файлы
:command! -complete=file -nargs=1 Rpdf :r !pdftotext -nopgbrk <q-args> - |fmt -csw78

"Отменяем выгрузку буфера при переключении на другой файл
set hidden

"Включаем нумерацию строк
set number

"Перенос длинных строк
set wrap

"Перенос по словам, а не по буквам
set linebreak

"Заменяем tab на 4 пробела
set tabstop=4

"Умные отступы
set smartindent

"Таб на 4 пробела
set expandtab

"Аналогично для >> и <<
set shiftwidth=4

"Включаем подсветку синтаксиса
syntax on

"Скрываем мышь в режиме ввода текста
set mousehide

"Открываем на полный экран
if has("gui_running")
  au GUIEnter * :set lines=99999 columns=99999
end

"Настройки для показывания Tab
set list

"Компиляция и запуск для С-программ
autocmd Filetype c source ~/vimconf/develop.vim
autocmd Filetype c source ~/vimconf/c.vim

"Настройки для ассемблерных файлов
autocmd Filetype asm source ~/vimconf/develop.vim
autocmd Filetype asm source ~/vimconf/asm.vim

"Настройки для puthon-файлов
autocmd Filetype python source ~/vimconf/develop.vim
autocmd Filetype python source ~/vimconf/python.vim

"Настройки для cpp-файлов
autocmd Filetype cpp source ~/vimconf/develop.vim
autocmd Filetype cpp source ~/vimconf/cpp.vim

"Настроим включение перевода на <F2>
map <F2> :source ~/vimconf/translate.vim<cr>
imap <F2> <Esc><F2>
vmap <F2> <Esc><F2>

"Новая вкладка по <C-t>
map <C-t> :tabnew<cr>
imap <C-t> <Esc><C-t>a
vmap <C-t> <Esc><C-t>v

"Следующая вкладка по <C-Tab>
map <C-Tab> :tabnext<cr>
imap <C-Tab> <Esc><C-Tab>a
vmap <C-Tab> <Esc><C-Tab>v

"Use Vim defaults instead of Vi compatibility
set nocompatible

"For backspace
set backspace=indent,eol,start

