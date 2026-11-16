const threats = [
{
id:1,
threat:"Phishing Campaign",
severity:"High",
ip:"192.168.1.10",
date:"2026-11-01"
},
{
id:2,
threat:"Ransomware Attack",
severity:"Critical",
ip:"185.23.44.10",
date:"2026-11-02"
},
{
id:3,
threat:"SQL Injection",
severity:"Medium",
ip:"101.45.23.11",
date:"2026-11-03"
},
{
id:4,
threat:"DDoS Attack",
severity:"Critical",
ip:"78.65.21.19",
date:"2026-11-04"
},
{
id:5,
threat:"Botnet Activity",
severity:"High",
ip:"201.44.11.78",
date:"2026-11-05"
}
];

const tbody =
document.getElementById("threatTableBody");

threats.forEach(item => {

tbody.innerHTML += `
<tr>
<td>${item.id}</td>
<td>${item.threat}</td>
<td>${item.severity}</td>
<td>${item.ip}</td>
<td>${item.date}</td>
</tr>
`;

});