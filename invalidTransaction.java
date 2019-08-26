import java.util.HashMap;
import java.lang.*;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        List<String> output = new ArrayList<String>();
        
        HashMap<String, String> hmap = new HashMap<String, String>();
        
        for(String transaction: transactions) {
            String[] list_tran = transaction.split(",");
            String name = list_tran[0];
            hmap.put(transaction, name);
        }
        
        for(String transaction: transactions) {
            String[] list_tran = transaction.split(",");
            String name = list_tran[0];
            int time = Integer.parseInt(list_tran[1]);
            int amount = Integer.parseInt(list_tran[2]);
            String city = list_tran[3];

            if(amount > 1000) {
                output.add(transaction);
                
            }
            
            for(Map.Entry<String, String> entry: hmap.entrySet()) {
                String tran = entry.getKey();
                String t_name = entry.getValue();
                if (!tran.equals(transaction) && t_name.equals(name)) {
                    String[] list_t = tran.split(",");
                    String place_t = list_t[3];
                    int time_t = Integer.parseInt(list_t[1]);
                    if ((Math.abs(time_t - time) <= 60) && (!city.equals(place_t))) {
                        if(!output.contains(transaction)) {
                        output.add(transaction);
                        }
                    }
                }
            }
            
            
        }
        return output;
        
    }
}
