<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KCVPC Setup Documentation</title>
</head>
<body>
    <h1>KCVPC Setup Documentation</h1>
    
    <p>This README.md file provides detailed instructions and explanations on setting up a Virtual Private Cloud (VPC) in AWS with both public and private subnets, routing configurations, security groups, and network access control lists (NACLs).</p>
    
    <h2>Objective</h2>
    <p>To design and implement a secure and efficient network architecture using AWS services, following best practices for communication and security within a VPC.</p>
    
    <p><a href="https://excalidraw.com/#json=V4D6DiCTBiHE3fRp9jEQ-,68OksBXoF4dNBWtN8BTSgw" target="_blank">Architecture Diagram</a></p>
    
    <h2>Steps to Create and Configure the VPC</h2>
    
    <ol>
        <li>
            <h3>Create a VPC</h3>
            <ul>
                <li>VPC Name: KCVPC</li>
                <li>IPv4 CIDR Block: 10.0.0.0/16</li>
            </ul>
            <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/KCVPC_Screenshot.png" target="_blank">Screenshot</a></p>
        </li>
        
        <li>
            <h3>Create Subnets</h3>
            <ul>
                <li>
                    Public Subnet
                    <ul>
                        <li>Name: PublicSubnet</li>
                        <li>IPv4 CIDR Block: 10.0.1.0/24</li>
                        <li>Availability Zone: Select any one (e.g., eu-west-1a)</li>
                    </ul>
                    <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/Public%20and%20Private%20Subnet_ss.png" target="_blank">Screenshot</a></p>
                </li>
                <li>
                    Private Subnet
                    <ul>
                        <li>Name: PrivateSubnet</li>
                        <li>IPv4 CIDR Block: 10.0.2.0/24</li>
                        <li>Availability Zone: Same as Public Subnet (e.g., eu-west-1a)</li>
                    </ul>
                </li>
            </ul>
        </li>
        
        <li>
            <h3>Configure an Internet Gateway (IGW)</h3>
            <ul>
                <li>Create IGW</li>
                <li>Attach IGW to KCVPC</li>
            </ul>
            <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/Public%20and%20Private%20Subnet_ss.png" target="_blank">Screenshot</a></p>
        </li>
        
        <li>
            <h3>Configure Route Tables</h3>
            <ul>
                <li>
                    Public Route Table
                    <ul>
                        <li>Name: PublicRouteTable</li>
                        <li>Associated Subnet: PublicSubnet</li>
                        <li>Route: 0.0.0.0/0 -&gt; IGW</li>
                    </ul>
                    <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/Pulic%20and%20Private%20Route%20Tables.png" target="_blank">Screenshot</a></p>
                </li>
                <li>
                    Private Route Table
                    <ul>
                        <li>Name: PrivateRouteTable</li>
                        <li>Associated Subnet: PrivateSubnet</li>
                        <li>Route: No direct route to the internet initially</li>
                    </ul>
                </li>
            </ul>
        </li>
        
        <li>
            <h3>Configure NAT Gateway</h3>
            <ul>
                <li>NAT Gateway Location: PublicSubnet</li>
                <li>Elastic IP Allocation: Allocate a new Elastic IP</li>
            </ul>
            <p>Update PrivateRouteTable to Route Traffic to NAT Gateway</p>
            <ul>
                <li>Route: 0.0.0.0/0 -&gt; NAT Gateway</li>
            </ul>
            <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/NAT-KCVPC.png" target="_blank">Screenshot</a></p>
        </li>
        
        <li>
            <h3>Set Up Security Groups</h3>
            <ul>
                <li>
                    Public Security Group
                    <ul>
                        <li>Allow Inbound:</li>
                        <ul>
                            <li>HTTP (Port 80) from 0.0.0.0/0</li>
                            <li>HTTPS (Port 443) from 0.0.0.0/0</li>
                            <li>SSH (Port 22) from your specific IP</li>
                        </ul>
                        <li>Allow Outbound: All traffic</li>
                    </ul>
                    <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/SG1-KCVPC.png" target="_blank">Screenshot</a></p>
                </li>
                <li>
                    Private Security Group
                    <ul>
                        <li>Allow Inbound: MySQL (Port 3306) from PublicSubnet</li>
                        <li>Allow Outbound: All traffic</li>
                    </ul>
                    <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/SG2-KCVPC.png" target="_blank">Screenshot</a></p>
                </li>
            </ul>
        </li>
        
        <li>
            <h3>Configure Network ACLs (NACLs)</h3>
            <ul>
                <li>
                    Public Subnet NACL
                    <ul>
                        <li>Inbound Rules:</li>
                        <ul>
                            <li>Allow HTTP (Port 80)</li>
                            <li>Allow HTTPS (Port 443)</li>
                            <li>Allow SSH (Port 22)</li>
                        </ul>
                        <li>Outbound Rules: Allow all traffic</li>
                    </ul>
                    <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/NACLs.png" target="_blank">Screenshot</a></p>
                </li>
                <li>
                    Private Subnet NACL
                    <ul>
                        <li>Inbound Rules: Allow traffic from Public Subnet</li>
                        <li>Outbound Rules: Allow traffic to Public Subnet and internet</li>
                    </ul>
                </li>
            </ul>
        </li>
        
        <li>
            <h3>Deploy Instances</h3>
            <ul>
                <li>EC2 Instance in PublicSubnet</li>
                <ul>
                    <li>Security Group: Public Security Group</li>
                    <li>Verification: Ensure access via the internet</li>
                </ul>
                <li>EC2 Instance in PrivateSubnet</li>
                <ul>
                    <li>Security Group: Private Security Group</li>
                    <li>Verification: Ensure internet access through the NAT Gateway and communication with the public instance</li>
                </ul>
            </ul>
            <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/EC2-KCVPC.png" target="_blank">EC2-KCVPC Screenshot</a></p>
            <p><a href="https://github.com/CkEvan/KcampTasks/blob/main/kcamptask5/EC2-connection.png" target="_blank">EC2-connection Screenshot</a></p>
        </li>
        
    </ol>
    
    <h2>Explanation of Components</h2>
    <dl>
        <dt>Virtual Private Cloud (VPC)</dt>
        <dd>A logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define.</dd>
        
        <dt>Subnets</dt>
        <dd>
            <ul>
                <li>Public Subnet: A subnet with a route to the internet via the Internet Gateway, allowing instances to be accessible from the internet.</li>
                <li>Private Subnet: A subnet without direct access to the internet, ensuring instances are only accessible within the VPC.</li>
            </ul>
        </dd>
        
        <dt>Internet Gateway (IGW)</dt>
        <dd>Enables communication between instances in the VPC and the internet.</dd>
        
        <dt>NAT Gateway</dt>
        <dd>Allows instances in a private subnet to connect to the internet or other AWS services, but prevents the internet from initiating connections with those
