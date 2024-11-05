import java.io.*;
import java.net.*;

public class ClientUDP {
    public static void main(String[] args) {
        try {
            InetAddress addr = InetAddress.getLocalHost();
            System.out.println("adresse=" + addr.getHostName());

            // Préparation du message à envoyer
            String s = "Hello World";
            byte[] data = s.getBytes();

            // Création du paquet et envoi au serveur
            DatagramPacket packet = new DatagramPacket(data, data.length, addr, 1234);
            DatagramSocket sock = new DatagramSocket();
            sock.send(packet);

            // Préparation de la réception de la réponse du serveur
            DatagramPacket responsePacket = new DatagramPacket(new byte[1024], 1024);
            sock.receive(responsePacket);

            // Affichage de la réponse du serveur
            String response = new String(responsePacket.getData(), 0, responsePacket.getLength());
            System.out.println("Réponse du serveur : " + response);

            // Fermeture du socket
            sock.close();
        } catch (Exception ex) {
            System.out.println("Erreur !");
            ex.printStackTrace();
        }
    }
}

