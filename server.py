from flask import Flask, jsonify, request
import os
import fitz  # PyMuPDF
from functions.PDF_Functions import extract_text_from_pdf, generate_resume_from_html
from functions.AI_Functions import generate_enhanced_resume
from dotenv import load_dotenv
load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")


app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the AI Resume Enhancer Backend!"})

# @app.route('/')
def generate_resume():
    extracted_text = extract_text_from_pdf("C:\\Users\\Admin\\Desktop\\Projects\\AI Resume\\backend\\AI_Resume_Enhancer_backend\\Aarav_Mehta_Blockchain_Resume.pdf")
    job_description = (
        "🧾 Job Description: Network Engineer\n"
        "Position: Network Engineer\n"
        "Location: Mumbai, India (Hybrid)\n"
        "Experience: 2–5 years\n"
        "Salary: ₹6–12 LPA\n"
        "Company: NetAxis Technologies – Leading provider of secure infrastructure solutions for enterprise clients.\n\n"
        "🧠 Role Summary\n"
        "We are seeking a skilled and motivated Network Engineer to design, implement, maintain, and support our growing network infrastructure. You will be part of a dynamic team responsible for managing both physical and cloud network environments, ensuring high availability, scalability, and security of all systems.\n\n"
        "🔧 Key Responsibilities\n"
        "Design and deploy functional and secure networks (LAN, WAN, WLAN, VPN)\n\n"
        "Monitor network performance and ensure system availability and reliability\n\n"
        "Configure and install network hardware (e.g., routers, switches, firewalls, load balancers)\n\n"
        "Troubleshoot network outages and provide Tier 2/3 support\n\n"
        "Maintain security by implementing firewalls, access controls, and VPNs\n\n"
        "Collaborate with infrastructure and cloud teams to optimize network connectivity\n\n"
        "Document network infrastructure, configurations, and maintenance procedures\n\n"
        "Perform regular backup operations and disaster recovery simulations\n\n"
        "🧰 Tech Stack & Tools\n"
        "Networking: TCP/IP, DNS, DHCP, VLAN, BGP, OSPF\n\n"
        "Hardware: Cisco, Juniper, Fortinet, Palo Alto\n\n"
        "Tools: Wireshark, SolarWinds, Nagios, Zabbix\n\n"
        "Cloud: AWS VPC, Azure Virtual Network, GCP Networking\n\n"
        "Security: Firewalls, VPN, IPS/IDS\n\n"
        "Scripting: Bash, Python (for automation and monitoring)\n\n"
        "DevOps Integration: Git, Ansible (optional)\n\n"
        "✅ Qualifications\n"
        "Bachelor’s degree in Computer Science, IT, or related field\n\n"
        "2+ years of hands-on experience in enterprise network administration\n\n"
        "Strong knowledge of networking protocols and security best practices\n\n"
        "Experience with cloud networking (AWS/Azure/GCP) is a plus\n\n"
        "Certifications like CCNA/CCNP or equivalent are highly desirable\n\n"
        "Excellent problem-solving and communication skills\n\n"
        "🌟 Nice to Have\n"
        "Experience with SD-WAN and Software Defined Networking (SDN)\n\n"
        "Knowledge of container networking (Docker, Kubernetes)\n\n"
        "Automation using Python or Ansible\n\n"
        "Participation in network architecture design discussions\n\n"
        "🏢 Why Join Us\n"
        "Work on cutting-edge hybrid network infrastructure projects\n\n"
        "Collaborative, growth-driven work culture\n\n"
        "Certification sponsorships and learning programs\n\n"
        "Competitive pay and flexible working model\n"
    )
    enhanced_resume = generate_enhanced_resume(job_description, extracted_text)
    return enhanced_resume
    # generate_resume_from_html(enhanced_resume)

@app.route("/upload", methods=["GET", "POST"])
def upload_resume():
    if 'file' not in request.files:
        return "No file part"
        
    file = request.files['file']
        
    if file.filename == '':
            return "No selected file"
        
    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        try:
            doc = fitz.open(filepath)
            extracted_resume = extract_text_from_pdf(doc)
            job_description = (
                "🧾 Job Description: Network Engineer\n"
                "Position: Network Engineer\n"
                "Location: Mumbai, India (Hybrid)\n"
                "Experience: 2–5 years\n"
                "Salary: ₹6–12 LPA\n"
                "Company: NetAxis Technologies – Leading provider of secure infrastructure solutions for enterprise clients.\n\n"
                "🧠 Role Summary\n"
                "We are seeking a skilled and motivated Network Engineer to design, implement, maintain, and support our growing network infrastructure. You will be part of a dynamic team responsible for managing both physical and cloud network environments, ensuring high availability, scalability, and security of all systems.\n\n"
                "🔧 Key Responsibilities\n"
                "Design and deploy functional and secure networks (LAN, WAN, WLAN, VPN)\n\n"
                "Monitor network performance and ensure system availability and reliability\n\n"
                "Configure and install network hardware (e.g., routers, switches, firewalls, load balancers)\n\n"
                "Troubleshoot network outages and provide Tier 2/3 support\n\n"
                "Maintain security by implementing firewalls, access controls, and VPNs\n\n"
                "Collaborate with infrastructure and cloud teams to optimize network connectivity\n\n"
                "Document network infrastructure, configurations, and maintenance procedures\n\n"
                "Perform regular backup operations and disaster recovery simulations\n\n"
                "🧰 Tech Stack & Tools\n"
                "Networking: TCP/IP, DNS, DHCP, VLAN, BGP, OSPF\n\n"
                "Hardware: Cisco, Juniper, Fortinet, Palo Alto\n\n"
                "Tools: Wireshark, SolarWinds, Nagios, Zabbix\n\n"
                "Cloud: AWS VPC, Azure Virtual Network, GCP Networking\n\n"
                "Security: Firewalls, VPN, IPS/IDS\n\n"
                "Scripting: Bash, Python (for automation and monitoring)\n\n"
                "DevOps Integration: Git, Ansible (optional)\n\n"
                "✅ Qualifications\n"
                "Bachelor’s degree in Computer Science, IT, or related field\n\n"
                "2+ years of hands-on experience in enterprise network administration\n\n"
                "Strong knowledge of networking protocols and security best practices\n\n"
                "Experience with cloud networking (AWS/Azure/GCP) is a plus\n\n")
            enhanced_resume = generate_enhanced_resume(job_description, extracted_resume)
            return enhanced_resume
        except Exception as e:
                return f"Error processing PDF with fitz: {e}"
    else:
        return "Invalid file type. Please upload a PDF."

if __name__ == '__main__':
    app.run(debug=True)