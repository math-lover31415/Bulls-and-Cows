import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;
class BullsAndCowsGUI extends JFrame implements ActionListener{
    static String key;
    static void init_key(){
        Random r = new Random();
        key = "";
        while (key.length()<4){
            char c = (char)(48+r.nextInt(10));
            if (key.indexOf(c)!=-1) continue;
            key += c;
        }
    }
    static{
        init_key();
    }

    void BullsAndCows(String s) throws Exception{
        bulls = 0;
        cows = 0;
        if (s.length()!=4) throw new Exception("Input should be 4 characters long");
        for (int i=0;i<4;i++){
            char c = s.charAt(i);
            if (c==key.charAt(i)) bulls++;
            if (c<'0' || c>'9') throw new Exception("Input should be numeric");
            for (int j=0;j<i;j++){
                if (c==s.charAt(j)){
                    throw new Exception("All numbers in input should be unique");
                }
                if (c==key.charAt(j)) cows++;
            }
            for (int j=i+1;j<4;j++) if (c==key.charAt(j)) cows++;
        }
    }

    JFrame jfrm;
    JButton new_game, enter;
    JLabel arr[][] = new JLabel[12][3];
    JLabel error;
    int current = 0;
    int bulls, cows;
    boolean ongoing = true;
    JTextField input;
    GridBagLayout gbag = new GridBagLayout();
    GridBagConstraints gbc = new GridBagConstraints();
    BullsAndCowsGUI(){
        jfrm = new JFrame("Bulls and Cows");
        jfrm.getContentPane().setBackground(Color.white);
        jfrm.setLayout(gbag);
        jfrm.setSize(500,500);
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        gbc.insets = new Insets(5,5,5,5);
        gbc.gridy = 0;
        gbc.gridx = 0;
        //gbc.fill = GridBagConstraints.BOTH;
        jfrm.add(new JLabel("Guess"),gbc);
        gbc.gridx = 1;
        jfrm.add(new JLabel("Bulls"),gbc);
        gbc.gridx = 2;
        jfrm.add(new JLabel("Cows"),gbc);
        for (int i=0;i<12;i++){
            gbc.gridy = i+1;
            for (int j=0;j<3;j++){
                arr[i][j] = new JLabel("    ");
                gbc.gridx = j;
                jfrm.add(arr[i][j],gbc);
            }
        }
        gbc.gridy = 13;
        gbc.gridx = 0;
        input = new JTextField(15);
        input.addActionListener(this);
        jfrm.add(input,gbc);

        gbc.gridx = 1;
        enter = new JButton("Enter");
        enter.addActionListener(this);
        jfrm.add(enter,gbc);

        gbc.gridx = 2;
        new_game = new JButton("New Game");
        new_game.addActionListener(this);
        jfrm.add(new_game,gbc);

        gbc.gridx = 0;
        gbc.gridy = 14;
        gbc.gridwidth = 3;
        error = new JLabel(" ");
        gbc.insets = new Insets(10,5,10,5);
        jfrm.add(error,gbc);

        jfrm.pack();
        jfrm.setLocationRelativeTo(null);
        jfrm.setVisible(true);
    }
    public void actionPerformed(ActionEvent ae){
        String s = ae.getActionCommand();
        if (s.equalsIgnoreCase("Enter") || s.equalsIgnoreCase(input.getText())){
            if (current>=12) return;
            String num = input.getText();
            input.setText("");
            try{
                BullsAndCows(num);
                arr[current][0].setText(num);
                arr[current][1].setText(Integer.toString(bulls));
                arr[current][2].setText(Integer.toString(cows));
                if (bulls==4){
                    current = 12;
                    error.setText("You won the game :)");
                }
                else current++;
                if (current==12 && bulls!=4){
                    error.setText("You lost the game :(");
                }
            } catch (Exception e){
                error.setText("Error: "+e.getMessage());
            }
        } else if(s.equalsIgnoreCase("New Game")){
            init_key();
            current = 0;
            for (int i=0;i<12;i++){
                for (int j=0;j<3;j++){
                    arr[i][j].setText(" ");
                }
            }
            error.setText(" ");
        } else {
            System.out.println(s);
        }
    }
    public static void main(String[] args){
        SwingUtilities.invokeLater(
            new Runnable(){
                public void run(){
                    new BullsAndCowsGUI();
                }
            }
        );
    }
}