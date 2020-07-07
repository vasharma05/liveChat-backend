var user = document.getElementById('liveChat').getAttribute('user-name')
var chatContainer = document.createElement('div')
chatContainer.id = 'chatContainer'
var iframe = document.createElement('iframe')
iframe.src = `http://localhost:3000/consumer/${user}/`
iframe.id='iframe'
chatContainer.appendChild(iframe)
var chatIconContainer = document.createElement('div')
chatIconContainer.id = 'chatIconContainer'
var img = document.createElement('img')
img.id='chatIcon'
img.src='http://localhost:8000/media/script/chaticon.svg'
chatIconContainer.appendChild(img)
chatContainer.appendChild(chatIconContainer)
var link = document.createElement('link')
link.rel = 'stylesheet'
link.href = 'http://localhost:8000/media/script/script.css'
document.head.appendChild(link)
document.body.appendChild(chatContainer) 
var open = false
chatIconContainer.addEventListener('click', (e)=>{
    open = !open
    document.querySelector('iframe').style.display = open ? 'block' : 'none' 
})
icon.addEventListener('click', (e)=>{
    open = !open
    document.querySelector('iframe').style.display = open ? 'block' : 'none' 
})