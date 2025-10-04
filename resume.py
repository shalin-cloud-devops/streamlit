import streamlit as st
import pandas as pd
import time as t

st.set_page_config(
    page_title="Senior DevOps Engineer Resume",
    page_icon="gear",
    layout="wide"
)

st.subheader("Summary")
st.markdown("""
Senior DevOps Engineer with 14+ years of experience, including over a year in New Zealand, building scalable infrastructure
and automated deployment pipelines for global financial institutions. Expert in CI/CD, SRE, cloud architecture, and
automation. Proven track record of optimizing performance and mentoring teams in DevOps best practices

---
""")

st.subheader("Experience")
st.markdown("""
###### Citibank (Citi) | Chennai
            
###### Senior DevOps Engineer | 09/2023 - Present
- Design and implement CI/CD pipelines using Tekton and Harness to improve software deployment speed and efficiency.
- Automate infrastructure and application deployments using Ansible and Python.
- Manage and maintain uDeploy processes and ensure Git repository hygiene and best practices.
- Apply SRE principles to enhance system reliability, monitoring, and performance.
- Support and configure middleware platforms, including Tomcat and WebLogic.
- Collaborate with development teams to troubleshoot issues and optimize application performance and reliability.
- Mentor junior engineers on DevOps tools, methodologies, and automation best practices.

---

###### HCL Technologies | Banglore & New Zealand
###### Consultant | 09/2017 - 09/2023       
- Worked as a Senior Middleware Consultant for a global bank, leading the design and delivery of Managed File Transfer
- (MFT) solutions.
- Managed a team of Cloud & MFT specialists and led a successful Project on migrating onprem MFT infrastructure to
AWS Cloud.
- Automated Connect Direct installations on AWS EC2 instances using Terraform
- Proficient with AWS services including EC2, S3, IAM, and VPC to build and manage cloud infrastructure.

---

###### Wipro | Bangalore
###### Senior Project Engineer | 01/2016 - 08/2017

- Served as a Senior Middleware Specialist
- Worked on Sterling Integrator, Cleo Harmony, and Connect Direct for a global bank.
- Supported the Sterling File Gateway (SFG) team and trained new team members on Connect Direct projects.
- Contributed to multiple RFPs at Wipro, helping secure key projects.

---

###### Future Focus
###### Developer | 07/2013 - 01/2016
- Started as a Middleware Developer, working extensively on all versions of Connect:Direct (C:D) for secure file transfers.
- Gained strong expertise in Control-M scheduling and advanced job design, supporting critical banking applications.
- Led projects from design through implementation, ensuring timely and reliable delivery of middleware and file transfer
solutions.
- Contributed to multiple data warehousing projects requiring advanced Control-M design for large-scale, mission-critical
banking systems.
- Provided MFT support for all critical applications of the bank, ensuring high availability and smooth operations.

---
            
###### TCS | Chennai
###### Process Associate | 03/2011 - 01/2013

- Worked as Windows support associate for an insurance conglomerate
- Responsible for Windows server related issues.
- Installing or upgrading Windows systems and servers.
- Metal Trading Company | Trichy
- Production Supervisor | 01/2011 - 01/2011
- Handled production scheduling and acted as the primary point of contact for clients.
- Collaborated with stakeholders in meetings and successfully won several projects.

---      
""")

left_panel = st.sidebar
left_panel.subheader("Skills")
left_panel.markdown("""
- DevOps
- Ansible 
- Control M 
- SRE 
- AWS 
- AutoSys 
- Tekton 
- UrbanCode Deploy 
- Terraform 
- Python 
- Harness 
- IBM Connect:Direct 
- Team Management 
- Agile 
- GIT

---

[Linkedin](https://www.linkedin.com/in/akbar-shalin/)
                    
<akbarshalin100@gmail.com>
                    
***+91 8951252205***
""")
