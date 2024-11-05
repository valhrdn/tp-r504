import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) {
        try {
            // Création du socket UDP sur le port 1234
            DatagramSocket sock = new DatagramSocket(1234);
            while (true) {
                System.out.println("- Waiting data");

                // Réception du message du client
                DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);
                sock.receive(packet);

                // Conversion des données reçues en chaîne de caractères et affichage
                String str = new String(packet.getData(), 0, packet.getLength());
                System.out.println("str=" + str);

                // Renvoi du message reçu au client
                DatagramPacket responsePacket = new DatagramPacket(
                    packet.getData(), packet.getLength(), packet.getAddress(), packet.getPort()
                );
                sock.send(responsePacket);
            }
        } catch (Exception e) {
            System.out.println("Erreur !");
            e.printStackTrace();
        }
    }
}

