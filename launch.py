import config
import monkey_trade as mt

def import_cfg():
    file_name = input('\nEnter the file name (ext. included): ')
    return config.Config(file_name)

def run_monkey():
    m = mt.MonkeyTrade(cfg.start_date, cfg.end_date, cfg.start_value, cfg.symbols)
    m.monkey_trade()
    print(m.show_results())
    return compare(m)

def compare(m):
    m_profit = round(float(m.prt.get_value(m.end_date) - m.start_value), 2)
    u_profit = cfg.end_value - cfg.start_value
    print(f'User profit: ${u_profit:,.2f}, Monkey profit: ${m_profit:,.2f}\n')
    if m_profit > u_profit:
        print('Monkey won 🐒')
    elif m_profit == u_profit:
        print('Monkey had the same performance as user 😇')
    else:
        print('User won 👤')

    repeat = input('Rerun monkey? (y/n): ')
    run_monkey() if repeat.lower() == 'y' else quit()

if __name__ == '__main__':
    cfg = import_cfg()
    print('\nConfig set up successfully. Summary:')
    print(cfg.show_cfg())
    start = input('Start monkey trading? (y/n): ')
    if start.lower() == 'y':
        run_monkey()
    else:
        quit()