## Ashya: IoT devices registry on Blockchain 
### Decentralized web application for registering IoT devices based on Blockchain.
A full description of this project you can find [here](https://github.com/CiscoBlockChain/EthExperiments/blob/master/KlugeAshay.md)


### To run this demo you need: 
- Raspberry Pi 3. You can order it from [here](https://www.amazon.de/dp/B07BFVYMJY/ref=asc_df_B07BFVYMJY58454054/?tag=googshopde-21&creative=22434&creativeASIN=B07BFVYMJY&linkCode=df0&hvadid=309008177512&hvpos=1o2&hvnetw=g&hvrand=14415320193451425642&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061139&hvtargid=pla-436476818288&th=1&psc=1&tag=&ref=&adgrpid=65257070361&hvpone=&hvptwo=&hvadid=309008177512&hvpos=1o2&hvnetw=g&hvrand=14415320193451425642&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061139&hvtargid=pla-436476818288)
- A simple [webcam](https://www.google.com/search?rlz=1C1CHBD_enDE756DE756&biw=1280&bih=578&tbm=shop&ei=7HBhXNGqKc2asAe42IfIDw&q=simple+web+camera+logitech&oq=simple+web+camera+logitech&gs_l=psy-ab.3...15777.17091.0.17342.7.7.0.0.0.0.120.542.6j1.7.0....0...1c.1.64.psy-ab..0.0.0....0.pPMYop3Q7Lw#spd=15610673823399521644) 
- If you are using windows: download and install a compatible [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) version on your computer.
- For Mac or Linux users you can SSH to your raspberry Pi directly from your command shell 

### 1- Setup your Raspberry Pi 3
#### 1.1 Install OS on the Raspberry Pi
1- Download the latest Raspbian stretch desktop image from [here](https://www.raspberrypi.org/downloads/raspbian/)


2- Write the image to the SD card, You will need to use an image writing tool like [Etcher](https://www.balena.io/etcher/) to install the image you have downloaded on your SD card.

3- Connect an SD card reader with the SD card inside to your computer.

4- Open Etcher and select from your hard drive the Raspberry Pi .img or  .zip file you wish to write to the SD card.

5- Select the SD card you wish to write your image to.

6- Review your selections and click 'Flash!' to begin writing data to the SD card.

7- Once the flash completed, insert the SD card into your raspberry Pi and turn it on.

8- Connect your raspberry pi to the internet and enable SSh interface.

9- Get the IP address of your raspberry pi by running `ifconfig` in the terminal.

10- Save the IP address for later.

### 2- Get [Docker](https://docs.docker.com/) 

#### 2.1 Download and install Docker for raspberry Pi:

Our web application will run inside a docker container, so in order to be able to run the web application you need to download and install [Docker](https://docs.docker.com/install/linux/docker-ce/debian/) on your raspberry pi.

Alternatively, you can install docker by running this command in the terminal:

`sudo curl -sSL https://get.docker.com | sh`

Or:

`curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh`

Verify that Docker CE is installed correctly by running
`
$ sudo docker run hello-world
`

 When the container runs, it prints an informational message (Hello from Docker!) and exits.
 
 ![](docker.png)
 
 #### 2.2 Install docker compose:

 Compose is a tool for defining and running multi-container Docker applications. With Compose, you will be able to run YAML file which   contains all the container need to configure our application's services. 
 
 `sudo apt-get install -y python python-pip`
 
 `sudo pip install docker-compose`
 
 `docker-compose build`
 
 PS: don't forget to write sudo when running docker commands, else you will get permission denied error. 

### 3- Run the application 

#### 3.1 Get Metamask
Metamask is a browser extension provides a user interface to manage identities on different sites and sign blockchain transactions.
In this demo, every new device is represented by a smart contract. So we will use Metamask to enable us to deploy smart contracts on the blockchain and register devices to [Ashya.io](https://ashya.io/) to be visible for subscribers.

You can get the extension from [Metamask](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn) 
A full guide for using Metamask you can find [here](https://medium.com/publicaio/a-complete-guide-to-using-metamask-updated-version-cd0d6f8c338f)

#### 3.2 Create an account on Kovan-testnetwork.

#### 3.3 Get some ether 
Once you create an account, get some fake ether from [Kovan testnet/Fauset](https://gitter.im/kovan-testnet/faucet) by signing in to this website and posting your account address in the chat box, you can request ether.

We now need to get the code from GitHub, in order to build our system. So first you will need to install Git in your Raspberry pi.

#### 3.4 SSH to Raspberry Pi
Establish SSH connection to your Raspberry Pi using PuTTY, insert the IP address of the raspberry pi in the host name field and then press open.

#### 3.5 Download Git on the Raspberry Pi

Run:

`sudo apt install git`


#### 3.6 Download this repository

On the command line go to a directory where you will remember (I use ~/Code for all my code, but feel free to customize as you desire),from there, run:

`git clone https://github.com/CiscoBlockChain/AshyaDeviceService.git `

This will download the entire repository you are currently reading.

Move to AshyaDeviceService by running 

`cd AshyaDeviceService`

Then run:

`sudo docker-compose up -d`

![](compose.png)

  Make sure you watch the screen until you start seeing all the containers get up. 
  
 #### 3.7 Create a device contract
 
 Open the web browser to the IP address of your Rpi
  
 Try to run through the menus and register your device in [Ashya.io](https://ashya.io/). 
 
 A metamask window will pop up to confirm the transaction on Kovan testnet. Press submit to create the Device.
  
 If everything goes well you should see this page:
 
 ![](device.png)
 
 #### 3.8 Optionally: Register your device on Ashya.io
 
 If you want the people to see your device and subscribe to the stream of data produced by your device, you cann press Register Device button and confirm the transaction. This will charge you a little more ether. 
 
 If the registration process goes fine, go to Ashya.io page and refresh it. You should see your device address listed in the page. 
 Press on your device address to go to adding suscribers page. 
 
 
 
 ![](register.png)
 
 Here you can add a callback URL which specifies where the recieved data should go to. 
 After adding a subscriber and submitting the transaction on Metamask, your Url will be listed in the suscribers list and the json   output recieved from the object recognition software will be sent in directly and realtime to this URL. 
 
 
 You can watch a full demonstration of running this project [here](https://www.youtube.com/watch?v=ROwVSwbi4Mo)
