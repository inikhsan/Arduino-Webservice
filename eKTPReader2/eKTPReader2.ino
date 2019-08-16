#include <Wire.h>
#include <Adafruit_NFCShield_I2C.h>
#include <SPI.h>

#define RELAY_ON (4)
#define ACCESS_DELAY 1000
#define DENIED_DELAY 1000
#define IRQ   (2)
#define RESET (3)  // Not connected by default on the NFC Shield

Adafruit_NFCShield_I2C nfc(IRQ, RESET);

void setup(void) {
  Serial.begin(115200);
  //Serial.println(">http://www.github.com/awangga/NFCReader");
  pinMode(RELAY_ON, OUTPUT);
  //digitalWrite(RELAY, HIGH);
  nfc.begin();

  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
    Serial.print(">Didn't find PN53x board, please close and open serial monitor. If problem still exist please check your wiring");
    while (1); // halt
  }
  
  // Got ok data, print it out!
  //Serial.print(">Found chip PN5"); Serial.println((versiondata>>24) & 0xFF, HEX); 
  //Serial.print(">Firmware ver. "); Serial.print((versiondata>>16) & 0xFF, DEC); 
  //Serial.print('.'); Serial.println((versiondata>>8) & 0xFF, DEC);
  
  // Set the max number of retry attempts to read from a card
  // This prevents us from waiting forever for a card, which is
  // the default behaviour of the PN532.
  nfc.setPassiveActivationRetries(0xFF);
  
  // configure board to read RFID tags
  nfc.SAMConfig();
    
  //Serial.println("Waiting for an ISO14443A card");
}

  uint8_t card1[] =  { 0x4, 0x36, 0x38, 0xB2, 0x21, 0x25, 0x80 };  //card 1 Ikhsan
  uint8_t card2[] =  { 0x5, 0x8A, 0x99, 0x1E, 0x59, 0x31, 0x0 };  //card 2 Maul
  uint8_t card3[] =  { 0x4, 0x5E, 0x91, 0xE2, 0x9E, 0x4F, 0x80 }; //card 3 Alit
  uint8_t card4[] =  { 0x4, 0x31, 0x57, 0x5A, 0x7D, 0x5B, 0x80 }; // card 4 Cahya 
  uint8_t card5[] =  { 0x4, 0x23, 0x24, 0xFA, 0x80, 0x5B, 0x80 }; //card 5 Raziq 
  uint8_t card6[] =  { 0x4, 0x1E, 0x60, 0x6A, 0xC6, 0x61, 0x80 }; //card 6 Pak Fachri
  uint8_t card7[] =  { 0x4, 0x1C, 0x2E, 0xA, 0x42, 0x2A, 0x80 }; //card 7 Pak Rolly
  uint8_t card8[] =  { 0x4, 0x60, 0x59, 0xCA, 0x5B, 0x2A, 0x80 }; //card 8 Adit 
  uint8_t card9[] =  { 0, 0, 0, 0, 0, 0, 0 }; //card 9 Rifa
  uint8_t card10[] =  { 0, 0, 0, 0, 0, 0, 0 }; //card 10 Faisal

void loop() {
  // put your main code here, to run repeatedly:
  boolean success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID

  uint8_t uidLength;        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
  unsigned long readID =0;

  // Wait for an ISO14443A type cards (Mifare, etc.).  When one is found
  // 'uid' will be populated with the UID, and uidLength will indicate
  // if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &uid[0], &uidLength);

  if (success) {
//    Serial.println("Found a card!");
    Serial.print("");
      for (uint8_t i=0; i < uidLength; i++) 
      {
        Serial.print("0x");Serial.print(uid[i],HEX); 
        readID += uid[i];
        if(i < (uidLength -1)){
          readID = readID << 8;
        }
      }

    int i=0;
    int card1matches=0;
    int card2matches=0;
    int card3matches=0;
    int card4matches=0;
    int card5matches=0;
    int card6matches=0;
    int card7matches=0;
    int card8matches=0;
    int card9matches=0;
    int card10matches=0;

    for(i=0;i<7;i++)
    {
      if(uid[i] == card1[i])
      {
        card1matches++;      
      }
      if(uid[i] == card2[i])
      {
        card2matches++;      
      }
      if(uid[i] == card3[i])
      {
        card3matches++;      
      }
      if(uid[i] == card4[i])
      {
        card4matches++;      
      }
      if(uid[i] == card5[i])
      {
        card5matches++;      
      }
      if(uid[i] == card6[i])
      {
        card6matches++;      
      }
      if(uid[i] == card7[i])
      {
        card7matches++;      
      }
      if(uid[i] == card8[i])
      {
        card8matches++;      
      }
      if(uid[i] == card9[i])
      {
        card9matches++;      
      }
      if(uid[i] == card10[i])
      {
        card10matches++;      
      }
    }

    if(card1matches == 7)
    {
      Unlock();
    }
    if(card2matches == 7)
    {
      Unlock();
    }
    if(card3matches == 7)
    {
      Unlock();
    }
    if(card4matches == 7)
    {
      Unlock();
    }
    if(card5matches == 7)
    {
      Unlock();
    }
    if(card6matches == 7)
    {
      Unlock();
    }
    if(card7matches == 7)
    {
      Unlock();
    }
    if(card8matches == 7)
    {
      Unlock();
    }
    if(card9matches == 7)
    {
      Unlock();
    }
    if(card10matches == 7)
    {
      Unlock();
    }

      delay(2000);
  }
  else
  {
    // PN532 probably timed out waiting for a card
    Serial.println("Timed out waiting for a card");
  }
}

void Unlock()
  {
        Serial.println("");
//        Serial.println("Unlocking!!");
        digitalWrite(RELAY_ON, LOW);
        delay(2000);
        digitalWrite(RELAY_ON, HIGH);
  }
