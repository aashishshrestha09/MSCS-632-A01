(* Calculate mean by summing elements and dividing by length *)
let mean lst =
  let sum = List.fold_left ( + ) 0 lst in
  float_of_int sum /. float_of_int (List.length lst)

(* Calculate median by sorting list and selecting middle element(s) *)
let median lst =
  let sorted = List.sort compare lst in
  let n = List.length sorted in
  if n mod 2 = 0 then
    (float_of_int (List.nth sorted (n/2 -1) + List.nth sorted (n/2))) /. 2.0
  else
    float_of_int (List.nth sorted (n/2))

(* Calculate mode(s) by building frequency list and filtering *)
let mode lst =
  let freqs =
    List.fold_left (fun acc x ->
      if List.mem_assoc x acc then
        (x, (List.assoc x acc) + 1)::(List.remove_assoc x acc)
      else (x, 1)::acc
    ) [] lst in
  let max_count = List.fold_left (fun acc (_,c) -> max acc c) 0 freqs in
  let modes = List.filter (fun (_,c) -> c = max_count && c > 1) freqs in
  if modes = [] then
    Printf.printf "No mode (all unique values)\n"
  else begin
    Printf.printf "Mode(s): ";
    List.iter (fun (v,_) -> Printf.printf "%d " v) modes;
    Printf.printf "(appeared %d times)\n" max_count
  end

(* Find minimum element using fold *)
let min lst = List.fold_left min max_int lst

(* Find maximum element using fold *)
let max lst = List.fold_left max min_int lst

(* Calculate standard deviation using variance formula *)
let std_dev lst mean_val =
  let variance =
    List.fold_left (fun acc x -> acc +. ((float x -. mean_val) ** 2.)) 0.0 lst
  in
  sqrt (variance /. float_of_int (List.length lst))

(* Main entry *)
let () =
  let data = [5;2;9;5;7;9] in
  let mean_val = mean data in
  Printf.printf "Mean: %.2f\n" mean_val;
  Printf.printf "Median: %.2f\n" (median data);
  mode data;
  Printf.printf "Min: %d\n" (min data);
  Printf.printf "Max: %d\n" (max data);
  Printf.printf "Range: %d\n" ((max data) - (min data));
  Printf.printf "Standard Deviation: %.2f\n" (std_dev data mean_val)
