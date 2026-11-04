async function load() {
  const res = await fetch("/api/notes");
  const notes = await res.json();
  document.getElementById("list").innerHTML = notes
    .map(n => `<li><b>${n.title}</b>: ${n.content}</li>`)
    .join("");
}

document.getElementById("form").onsubmit = async (e) => {
  e.preventDefault();
  await fetch("/api/notes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: document.getElementById("title").value,
      content: document.getElementById("content").value,
    }),
  });
  e.target.reset();
  load();
};

load();