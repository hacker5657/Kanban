const selects = document.querySelectorAll('#select')

selects.forEach(select => {
	select.addEventListener('input', ()=>{
		select.parentNode.submit()
	})
})